# Importul bibliotecii care "știe" să lucreze cu BD SQLite
import sqlite3
# Importul bibliotecii care "știe" să deschidă site-uri în browser
import webbrowser

# Creăm obiectul-conexiune la BD
connection = sqlite3.connect('air.db')
# Creăm obiectul-cursor, prin care se pot executa interogări SQL
cursor = connection.cursor()

while True:
    city = input('Introduceți orașul:')

    if city == 'stop':
        break
    
    # Executăm o interogare SQL care va returna lista aeroporturilor din oraș
    cursor.execute('Select * from airports where city_eng=?', (city,))
    # salvăm înregistrări în forma de matrice
    x = cursor.fetchall()

    # # x = [['Chișinău', 'Chișinău,com'], ['Frankfurt', '.....' ]] - matrice 
    # # x[0][1]

    if len(x) == 0:
        print('Nu au fost găsite aeroporturi în orașul {}'.format(city))
    elif len(x) == 1: # În oraș există numai un singur aeroport  
        web_site = x[0][-1] 
        if web_site is None:
            print('Aeroportul din orașul {} nu are un site web'.format(city))
        else:
            webbrowser.open(web_site)
    else: # În oraș sunt mai multe aeroporturi
        result = '' #lista pregătită pentru utilizător 
        count = 0 # câte aeroporturi sunt 
        for aeroport in x:
            count += 1
            if result != '':
                result += '\n'
            result = str(count) + '-' + aeroport[1]
            print(result)

# 1 - Berlin International Airport\n
# 2 - Berlin Airport\n
# 3 - ....


# Închidem conexiunea cu BD
connection.close()