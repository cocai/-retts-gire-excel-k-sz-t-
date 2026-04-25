import pandas as pd
from datetime import datetime, timedelta

# idő átalakítás
def ido_pars(ido):
    return datetime.strptime(ido, "%H:%M")

def excel_elokeszito(hany_diak):
    """
    print("=" * 40)
    print("A tantárgynál rövidítéseket adj meg pl.: T(töri), I(irodalom), In(Idegen nyelv)")
    print("=" * 40)
    """
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

def excel_befejezo():
    df = pd.read_excel("Erettsegi_lista.xlsx")
    felelet_kezd = []
    felelet_vege = []

    for i in range(len(df)):
        base = ido_pars(df.loc[i, "Behívás ideje"])
        if df.loc[i, "Tantárgy"] == "In":
            fk_end = base + timedelta(minutes=0)
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


hany_diak_erettsegizik = int(input("Add meg hány diák érettségizik: "))
print("=" * 40)
print("A tantárgynál rövidítéseket adj meg pl.: T(töri), I(irodalom), In(Idegen nyelv)")
print("=" * 40)
excel_elokeszito(hany_diak_erettsegizik)

excel_befejezo()
print("Az excel fájl létrejött")
