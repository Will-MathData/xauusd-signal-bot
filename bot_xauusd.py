import pandas as pd
import matplotlib.pyplot as plt

# 1. DATA HISTORIS XAU/USD SELAMA 15 HARI
data_gold = {
    'Hari': list(range(1, 16)),
    'Harga': [2300, 2305, 2310, 2295, 2290, 2300, 2315, 2325, 2330, 2320, 2310, 2305, 2315, 2335, 2350]
}
df_gold = pd.DataFrame(data_gold)

# 2. MENGHITUNG MOVING AVERAGE (SMA)
# SMA 3-Hari (Garis Cepat)
df_gold['SMA_Cepat_3'] = df_gold['Harga'].rolling(window=3).mean()
# SMA 5-Hari (Garis Lambat)
df_gold['SMA_Lambat_5'] = df_gold['Harga'].rolling(window=5).mean()

# 3. SCANNER SINYAL TRADING (Golden Cross & Death Cross)
print("=== SCANNER SINYAL TRADING XAU/USD ===")
print("Mencari persilangan Moving Average (Golden Cross & Death Cross)...\n")

for i in range(1, len(df_gold)):
    if pd.notna(df_gold['SMA_Cepat_3'].iloc[i]) and pd.notna(df_gold['SMA_Lambat_5'].iloc[i]):
        
        # LOGIKA GOLDEN CROSS (Sinyal BUY)
        if (df_gold['SMA_Cepat_3'].iloc[i] > df_gold['SMA_Lambat_5'].iloc[i]) and \
           (df_gold['SMA_Cepat_3'].iloc[i-1] <= df_gold['SMA_Lambat_5'].iloc[i-1]):
            hari = df_gold['Hari'].iloc[i]
            harga = df_gold['Harga'].iloc[i]
            print(f"🟢 [HARI KE-{hari}] BOS! Waktunya BUY! (Golden Cross) di harga ${harga}")

        # LOGIKA DEATH CROSS (Sinyal SELL)
        elif (df_gold['SMA_Cepat_3'].iloc[i] < df_gold['SMA_Lambat_5'].iloc[i]) and \
             (df_gold['SMA_Cepat_3'].iloc[i-1] >= df_gold['SMA_Lambat_5'].iloc[i-1]):
            hari = df_gold['Hari'].iloc[i]
            harga = df_gold['Harga'].iloc[i]
            print(f"🔴 [HARI KE-{hari}] BOS! Waktunya SELL! (Death Cross) di harga ${harga}")

print("\nScan selesai, Bos!\n")

# 4. VISUALISASI GRAFIK ALGORITMA
plt.figure(figsize=(12, 6))

plt.plot(df_gold['Hari'], df_gold['Harga'], label='Harga XAU/USD', marker='o', color='gold', linewidth=3)
plt.plot(df_gold['Hari'], df_gold['SMA_Cepat_3'], label='SMA Cepat (3 Hari)', color='blue', linestyle='--', linewidth=2)
plt.plot(df_gold['Hari'], df_gold['SMA_Lambat_5'], label='SMA Lambat (5 Hari)', color='red', linestyle='-.', linewidth=2)

plt.title('Algoritma Sinyal Trading XAU/USD (Moving Average Crossover)', fontsize=15, fontweight='bold')
plt.xlabel('Hari Ke-', fontsize=12)
plt.ylabel('Harga (USD)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

# Tampilkan grafik
plt.show()
