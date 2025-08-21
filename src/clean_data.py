import pandas as pd

def clean_poverty_data(file_path):
    df = pd.read_csv(file_path, skiprows=4)
    df = df.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                 var_name='Year', value_name='Poverty Rate')
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    return df.dropna(subset=['Poverty Rate', 'Year'])