import pandas as pd
import numpy as np
import os

# --- Sri Lankan districts list ---
districts = [
    "Colombo","Gampaha","Kalutara","Kandy","Matale","Nuwara Eliya",
    "Galle","Matara","Hambantota","Jaffna","Kilinochchi","Mannar",
    "Vavuniya","Mullaitivu","Batticaloa","Ampara","Trincomalee",
    "Kurunegala","Puttalam","Anuradhapura","Polonnaruwa",
    "Badulla","Monaragala","Ratnapura","Kegalle"
]

months = list(range(1, 13))
years = list(range(2018, 2025))

rows = []

# --- Generate synthetic data ---
for district in districts:
    for year in years:
        for month in months:
            rainfall = np.random.uniform(50, 350)
            temp = np.random.uniform(22, 34)
            humidity = np.random.uniform(60, 95)
            population_density = np.random.uniform(300, 7000)
            dengue_cases = int(np.random.poisson(lam=rainfall/15 + humidity/10))
            outbreak = 1 if dengue_cases > 50 else 0

            rows.append([
                district, year, month, rainfall, temp, humidity,
                population_density, dengue_cases, outbreak
            ])

# --- Create DataFrame ---
df = pd.DataFrame(rows, columns=[
    "District", "Year", "Month", "Rainfall_mm", "Temperature_C",
    "Humidity_pct", "Population_Density", "Dengue_Cases", "Outbreak"
])

# --- Ensure save directory exists (Windows-friendly) ---
save_dir = "data"
os.makedirs(save_dir, exist_ok=True)
file_path = os.path.join(save_dir, "sri_lanka_dengue_extended.csv")

# --- Save CSV ---
df.to_csv(file_path, index=False)
print(f"Dataset successfully saved to {file_path}")
