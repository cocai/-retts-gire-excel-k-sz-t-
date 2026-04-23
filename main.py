import pandas as pd
from datetime import datetime, timedelta

# Excel beolvasás
df = pd.read_excel("Erettsegi_lista.xlsx")

# idő átalakítás
def ido_pars(ido):
    return datetime.strptime(ido, "%H:%M")


#felkeszules_kezd = []
felelet_kezd = []
felelet_vege = []

for i in range(len(df)):
    base = ido_pars(df.loc[i, "Behívás ideje"])
    if df.loc[i, "Tantárgy"] == "In":
        fk_end = base + timedelta(minutes=15)
        felelet_end = base + timedelta(minutes=15)
    else:
        #fk_start = base + timedelta(minutes=5)
        fk_end = base + timedelta(minutes=30)
        felelet_end = fk_end + timedelta(minutes=15)

    #felkeszules_kezd.append(fk_start.strftime("%H:%M"))
    felelet_kezd.append(fk_end.strftime("%H:%M"))
    felelet_vege.append(felelet_end.strftime("%H:%M"))

# új oszlopok hozzáadása
#df["Felkészülés kezdete"] = felkeszules_kezd
df["Felelet kezdete"] = felelet_kezd
df["Felelet vége"] = felelet_vege

# mentés
df.to_excel("Erettsegi_kesz.xlsx", index=False)

print(df)