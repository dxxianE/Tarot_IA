import pandas as pd

#excel to json with pandas
file_path = r'F:\GitHub\Tarot_IA\BD-tarot\Barajas\Estandar_es\bd_tarot_sig_img.xlsx'  
df = pd.read_excel(file_path)

#dataFrame a formato JSON
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

json_file_path = r'F:\GitHub\Tarot_IA\BD-tarot\Barajas\Estandar_es\bd_tarot_sig_img.json'  
with open(json_file_path, 'w', encoding='utf-8') as file:
    file.write(json_data)

print(f"Archivo JSON guardado en: {json_file_path}")
