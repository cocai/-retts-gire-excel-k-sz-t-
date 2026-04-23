import pandas as pd
from datetime import datetime, timedelta

""" 
-> Ember neve 
-> Behívás időpontja (Kezdési idő pl.: 8:00, 15pt nő) 
-> Tételhúzás (+2p pl.: 8:02) 
-> Felkészülés kezdete (+3p pl.: 8:05) 
-> Felkészülés vége és felelet kezdete: (+25p pl.: 8:30) 
-> Felelet vége: (+15p pl.: 8:45) 

"""

import pandas as pd
from datetime import datetime, timedelta

def ido_pars(ido):
    return datetime.strptime(ido, "%H:%M")

print("=" * 40)
print("A tantárgynál rövidítéseket adj meg pl.: T(töri), I(irodalom), In(Idegen nyelv)")
print("=" * 40)
hany_diak = int(input("Hány diák érettségizik?: "))
tantargy = []
diak_lista = []
for i in range(hany_diak):
    nev = input("Add meg a diák nevét: ")
    tan = input("Add meg a tantárgy nevét: ")
    diak_lista.append(nev)
    tantargy.append(tan)

# indulás
aktualis_ido = datetime.strptime("08:00", "%H:%M")
kovi_diak = []

for i in range(hany_diak):
    # minden diák kezdete
    base = aktualis_ido
    # következő diák = +15 perc (vagy amennyi kell)
    aktualis_ido = base + timedelta(minutes=15)
    kovi_diak.append(base.strftime("%H:%M"))

# DataFrame újraépítés
df = pd.DataFrame({
    "Diák neve": diak_lista,
    "Behívás ideje": kovi_diak,
    "Tantárgy": tantargy,
})

df.to_excel("Erettsegi_lista.xlsx", index=False)