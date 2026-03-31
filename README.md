# 💊 Načítanie abecedného zoznamu kategorizovaných liekov

Jednoduchý Python nástroj na efektívnu prácu s dátami z oficiálneho zoznamu kategorizácie liekov Ministerstva zdravotníctva SR.

## ✨ Vlastnosti
- **Automatické čistenie**: Odstraňuje nadbytočné biele znaky a nové riadky z hlavičiek Excel súboru.
- **Konverzia mien**: Automaticky transformuje slovenský formát cien (s čiarkou) na desatinné čísla (`float`) pre matematické operácie.
- **Efektívne vyhľadávanie**: Predpripravené funkcie na hľadanie podľa **ŠÚKL kódu** alebo **ATC skupiny**.

## 🛠️ Inštalácia a spustenie

### 1. Klonovanie repozitára
```bash
git clone https://github.com/jurzon/lekaren-kategorizacia.git
cd lekaren-kategorizacia
```

### 2. Príprava prostredia
Vytvorte si virtuálne prostredie a aktivujte ho podľa vášho operačného systému:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Inštalácia závislostí
Nainštalujte potrebné knižnice (Pandas, Openpyxl):
```bash
pip install -r requirements.txt
```

### 4. Spustenie programu
Uistite sa, že sa v koreňovom priečinku nachádza príslušný Excel súbor (`cast_I_abc_zoznam_liekov_N_k_01_04_2026.xlsx`) a spustite hlavný skript:
```bash
python main.py
```

## 📋 Požiadavky
- **Python 3.10+**
- **Pandas**: Na manipuláciu a analýzu dát.
- **Openpyxl**: Nevyhnutné pre čítanie moderných Excel súborov (`.xlsx`).

## 📂 Štruktúra projektu
- `main.py` - Hlavný aplikačný skript s logikou na spracovanie dát.
- `requirements.txt` - Zoznam potrebných Python knižníc.
- `.gitignore` - Konfigurácia pre Git, ktorá ignoruje `.venv`, `.vscode` a cache súbory.
- `cast_I_abc_...xlsx` - Vzorový dátový súbor kategorizácie liekov (ponechaný v repozitári ako výnimka v Gite pre ukážku).

---
*Vytvorené pre uľahčenie práce s farmaceutickými dátami v prostredí Python.*