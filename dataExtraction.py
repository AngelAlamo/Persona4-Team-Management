import pandas as pd
import urllib.request

url: str = "https://megamitensei.fandom.com/wiki/List_of_Persona_4_Personas";

""" Request url """
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url)

""" Obtain data """

df_list: pd.DataFrame = pd.read_html(url)[0:24];

lista_personas = [];

for i in range(0, 23):
    list_arcana = df_list[i][['Persona', 'Persona.1', 'Persona.2', 'Persona.3']];
    print(list_arcana);
    
    for j in range(0, len(list_arcana)):
        lista_personas += [x for x in list_arcana.iloc[j] if pd.isnull(x) == False and x != "nan"];


lista_personas.append(df_list[23]["Persona"].iloc[0]);

print(lista_personas);

print(len(lista_personas))