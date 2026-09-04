import pandas as pd

mapa_regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

caminho_vagas = "../df_vagas_2023.csv"
df_vagas = pd.read_csv(caminho_vagas, sep=',', encoding='utf-8', on_bad_lines='skip')
df_nodes = df_vagas[['ID_CURSO', 'NO_CURSO', 'SG_IES', 'SG_UF_CAMPUS']].drop_duplicates(subset=['ID_CURSO']).copy()
df_nodes['Id'] = df_nodes['ID_CURSO']
df_nodes['Label'] = df_nodes['NO_CURSO'] + " - " + df_nodes['SG_IES']
df_nodes['Regiao'] = df_nodes['SG_UF_CAMPUS'].map(mapa_regioes)
df_nodes.rename(columns={'SG_UF_CAMPUS': 'UF'}, inplace=True)
df_gephi = df_nodes[['Id', 'Label', 'UF', 'Regiao']]
df_gephi.to_csv("gephi_nodes_regioes.csv", index=False, encoding='utf-8')

print(f"{len(df_gephi)} nós exportados para 'gephi_nodes_regioes.csv'.")