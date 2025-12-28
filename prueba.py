import pandas as pd

# Esta es la ruta que pide tu metodología (data/raw)
archivo = "data/raw/DEMO25Q1.txt"

try:
    # solo 5 renglones para probar la ingesta inicial
    df = pd.read_csv(archivo, sep='$', nrows=10)
    print("completada")
    print("Datos encontrados en FAERS:")
    print(df[['primaryid', 'caseid', 'age']])
except Exception as e:
    print(f"Revisa el nombre del archivo: {e}")
