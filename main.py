exchange_rates = {
    'USD': {'BDT': 108.23, 'EUR': 0.92, 'CNY': 7.18, 'RUB': 84.18},
    'BDT': {'USD': 0.0092, 'EUR': 0.0085, 'CNY': 0.067, 'RUB': 0.79},
    'EUR': {'USD': 1.09, 'BDT': 117.55, 'CNY': 7.85, 'RUB': 92.52},
    'CNY': {'USD': 0.14, 'BDT': 14.97, 'EUR': 0.13, 'RUB': 11.79},
    'RUB': {'USD': 0.012, 'BDT': 1.29, 'EUR': 0.011, 'CNY': 0.086}
}
def converted_currency(amount, from_cur, to_cur):
    if from_cur == to_cur:
        return amount

    if from_cur in exchange_rates and to_cur in exchange_rates[from_cur]:
        conversion_rate = exchange_rates[from_cur][to_cur]
        converted_amount = amount * conversion_rate
        return converted_amount
    return

amount = float(input("Enter your amount: "))

from_cur = input("Which currency you want to covert from?\nBDT\nUSD\nEUR\nRUB\nCNY\n"
                     "(Type the currency name accordingly): ").upper()

to_cur = input("Which currency you want to covert to?\nBDT\nUSD\nEUR\nRUB\nCNY\n"
                   "(Type the currency name accordingly): ").upper()

converted_amount = converted_currency(amount, from_cur, to_cur)

if converted_amount:
    print(f"{amount} {from_cur} is equal to {converted_amount} {to_cur}")
else:
    print("Conversion failed. Please try again.")










