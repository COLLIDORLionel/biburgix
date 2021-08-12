
burgers = [
    ["ham", "le hamburger", 7.0],
    ["chb", "le cheeseburger", 7.5],
    ["bak", "le bakon burger", 7.5],
    ["bkc", "le bakon cheeseburger", 8.0],
    ["chi", "le chicken burger", 7.5],
    ["ccb", "le chicken cheeseburger", 8.0],
    ["veg", "le veggi burger", 8.0],
]


def menu():
    print("****** Biburgix Administration *****")
    print("1. Lister les burgers"
          "\n2. Ajouter un nouveau burger"
          "\n3. Mettre à jour un burger"
          "\n4. Supprimer un burger"
          "\n99. Sortir\n")


def get_all_burger():
    burgers_list = ""
    for burger in burgers:
        burgers_list += f"{burger[0].upper()} -> {burger[1].title()} ({burger[2]} €)\n"

    return burgers_list


def create_burger():
    code = input("Saisissez le code du nouveau burger : ").lower()
    name = input("Saisissez le nom du nouveau burger : ").lower()
    price = float(input("Saisissez le prix du nouveau burger : "))

    burgers.append([code, name, price])


def main():
    choice = 0
    while choice != "99":
        menu()
        choice = input()

        if choice == "1":
            print(get_all_burger())
        elif choice == "2":
            create_burger()
        elif choice == "99":
            print("Au revoir !")
            exit()


if __name__ == "__main__":
    main()
