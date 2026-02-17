import requests

api_key = "d8d1d6410c2d7ac08e9cd55a"

def convert(source, dest, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{source}"

    source = source.upper()
    dest = dest.upper()
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if dest in data["conversion_rates"]:
            currency = data["conversion_rates"][dest]
            sums = amount * currency
            print(f"{amount} {source} = {sums:.2f} {dest}")
        else:
            print("Could not find destination")
    except requests.exceptions.RequestException as e:
        print(e)


def main():
    source = input("Enter the currency you would like to convert: ")
    dest = input("Enter the currency to convert: ")
    amount = float(input("Enter the amount to convert: "))
    convert(source, dest, amount)

if __name__ == "__main__":
    main()