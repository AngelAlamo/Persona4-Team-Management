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
    
    for j in range(0, len(list_arcana)):
        lista_personas += [str(x).replace(" ", "_") for x in list_arcana.iloc[j] if pd.isnull(x) == False and x != "nan"];


lista_personas.append(df_list[23]["Persona"].iloc[0]);

# print(lista_personas);
# print(len(lista_personas))    226

remove_personas = ['Jiraiya', 'Susano-o', 'Takehaya_Susano-o', 'Konohana_Sakuya', 'Amaterasu', 'Sumeo-Okami',
                   'Take-Mikazuchi', 'Rokuten_Maoh', 'Takeji_Zaiten', 'Himiko', 'Kanzeon', 'Kouzeon', 'Tomoe',
                   'Suzuka_Gongen', 'Haraedo-no-Okami', 'Sukuna-Hikona', 'Yamato-Takeru', 'Yamato_Sumeragi',
                   'Kintoki-Douji', 'Kamui', 'Kamui-Moshiri']

# print(f'Len remove personas: {len(remove_personas)}');

for persona in remove_personas:
    try: 
        lista_personas.remove(persona);
    except ValueError:
        print(f'Persona {persona} not in lista personas');
        

# print(f'Len lista personas final: {len(lista_personas)}');


# ---------------------- Stats ----------------------

df_personas_stats = pd.DataFrame(columns = ['Persona', 'Arcana', '物', '火', '氷', '雷', '風', '光', '闇']);

list_arcana = ['Fool', 'Magician', 'Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Justice',
               'Hermit', 'Fortune', 'Strength', 'Hanged Man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 
               'Jester', 'Aeon', 'Judgement', 'World']


ids = [str(x) for x in range(0, 19+1)] + ["91", "90", "20", "21"]

j = 0;
for id in ids:
    url_stats: str = "https://p4g.gamekouryaku-no-ki.com/arcana?id=" + id;

    """ Request url """
    urllib.request.urlretrieve(url_stats)
    list_df = pd.read_html(url_stats)   # Los pares son datos

    print(list_df)

    i = 0;
    while i < len(list_df):
        df_personas_stats.loc[j] = {'Persona': lista_personas[j], 'Arcana': list_arcana[ids.index(id)], '物': list_df[i]['物'][0], '火': list_df[i]['火'][0], 
                                '氷': list_df[i]['氷'][0], '雷': list_df[i]['雷'][0], '風': list_df[i]['風'][0], '光': list_df[i]['光'][0], 
                                '闇':list_df[i]['闇'][0]}
        i += 2;
        j += 1;


print(df_personas_stats)    # Tabla final

print(len(df_personas_stats));  # 205


# ---------------------- Excel ----------------------
with pd.ExcelWriter('datos_personas_stats.xlsx', engine='xlsxwriter') as writer:
    df_personas_stats.to_excel(writer, sheet_name='Hoja1', index=False)

print("Archivo creado")
