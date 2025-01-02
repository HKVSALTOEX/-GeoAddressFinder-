import requests
from colorama import init, Fore

def get_address(latitude, longitude):
    headers = {
        'User-Agent': 'MyApp (altox1597@gmail.com)'
    }
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'display_name' in data:
            return data['display_name']
        else:
            return "Aucune adresse trouvée pour ces coordonnées."
    else:
        return f"Erreur lors de la requête : {response.status_code}"

def main():
    init(autoreset=True)
    while True:
        try:
            latitude = float(input(Fore.RED + "Entrez la latitude : "))
            longitude = float(input(Fore.RED + "Entrez la longitude : "))

            adresse = get_address(latitude, longitude)
            print(Fore.RED + f"Adresse : {adresse}")

            quitter = input(Fore.RED + "Appuyez sur Entrée pour quitter ou tapez n'importe quoi pour continuer : ")
            if quitter == "":
                print(Fore.RED + "\nProgramme terminé.")
                break
        except ValueError:
            print(Fore.RED + "Veuillez entrer des valeurs numériques valides pour la latitude et la longitude.")
        except KeyboardInterrupt:
            print(Fore.RED + "\nProgramme terminé.")
            break

if __name__ == "__main__":
    main()