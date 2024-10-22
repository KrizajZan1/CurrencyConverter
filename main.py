import requests

def pridobi_tecaje():
    url = "https://api.exchangerate.host/latest?base=EUR"
    response = requests.get(url)
    podatki = response.json()
    return podatki.get("rates")

def pretvori_valuto(tecaji, osnovna_valuta, ciljna_valuta, znesek):
    if osnovna_valuta != "EUR":
        znesek_v_eur = znesek / tecaji.get(osnovna_valuta, 1)
    else:
        znesek_v_eur = znesek
    
    pretvorjeni_znesek = znesek_v_eur * tecaji.get(ciljna_valuta, 1)
    return pretvorjeni_znesek

tecaji = pridobi_tecaje()

osnovna_valuta = input("Vnesi osnovno valuto (npr. EUR): ").upper()
ciljna_valuta = input("Vnesi ciljno valuto (npr. USD): ").upper()
znesek = float(input("Vnesi znesek za pretvorbo: "))

if osnovna_valuta in tecaji and ciljna_valuta in tecaji:
    pretvorjeni_znesek = pretvori_valuto(tecaji, osnovna_valuta, ciljna_valuta, znesek)
    print(f"{znesek} {osnovna_valuta} je enako {pretvorjeni_znesek:.2f} {ciljna_valuta}")
else:
    print("Neveljavna valuta. Preveri vnose in poskusi znova.")
