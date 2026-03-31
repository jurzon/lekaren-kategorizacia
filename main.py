import pandas as pd
import os

# 1. Presný názov súboru, ktorý vidí Python vo vašom priečinku
file_name = 'cast_I_abc_zoznam_liekov_N_k_01_04_2026.xlsx'

def nacitaj_a_spracuj():
    if not os.path.exists(file_name):
        print(f"❌ CHYBA: Súbor '{file_name}' nebol nájdený!")
        return

    print(f"✅ Súbor nájdený, načítavam Excel...")

    try:
        # ZMENA: Používame read_excel namiesto read_csv
        df = pd.read_excel(file_name)

        # Vyčistenie názvov stĺpcov
        df.columns = [str(c).replace('\n', ' ').strip() for c in df.columns]

        # Pri Exceli Pandas zvyčajne rozpozná čísla automaticky, 
        # ale pre istotu skúsime vyčistiť tie najdôležitejšie
        numeric_cols = ['Konečná c.', 'ÚZP', 'DOP']
        for col in numeric_cols:
            if col in df.columns and df[col].dtype == 'object':
                df[col] = df[col].str.replace(',', '.').astype(float)

        print("\n--- Prvých 5 riadkov ---")
        # Výpis stĺpca 'Kód' (kód lieku) a 'ATC' (prvý stĺpec)
        # Nastav si stĺpce podľa svojej potreby
        #zobrazenie = df[['ATC', 'Kód', 'Názov', 'Doplnok', 'Konečná c.']].head()
        zobrazenie = df[['Kód', 'Názov']].head()
        print(zobrazenie)
        
        return df

    except Exception as e:
        print(f"❌ Nastala chyba pri spracovaní: {e}")

if __name__ == "__main__":
    data = nacitaj_a_spracuj()
    
    if data is not None:
        # Príklad: Vyhľadáme liek podľa kódu lieku (stĺpec Kód)
        kod_na_hladanie = '6173B'
        vysledok = data[data['Kód'] == kod_na_hladanie]
        
        if not vysledok.empty:
            print(f"\nÚspech! Nájdený liek: {vysledok['Názov'].values[0]}")