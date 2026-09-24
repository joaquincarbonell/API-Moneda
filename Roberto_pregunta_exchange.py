import requests

respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
datos = respuesta.json()

tasas = datos["rates"]

moneda_mas_debil = max(tasas, key=tasas.get)
valor = tasas[moneda_mas_debil]

print("La moneda con más unidades por 1 EUR es:", moneda_mas_debil)
print("1 EUR =", valor, moneda_mas_debil)