

def show_menu():
    print("****** Biburgix Administration *****")
    print("1. Lister les burgers"
          "\n2. Ajouter un nouveau burger"
          "\n3. Mettre à jour un burger"
          "\n4. Supprimer un burger"
          "\n99. Sortir\n")


def get_all_burger(burgers):
    burgers_detail = ""
    for burger in burgers:
        burgers_detail += f"{burger[0].upper()} -> {burger[1].title()} ({burger[2]} €)\n"

    return burgers_detail


def create_burger(burgers):
    code = input("Saisissez le code du nouveau burger : ").lower()
    name = input("Saisissez le nom du nouveau burger : ").lower()
    price = float(input("Saisissez le prix du nouveau burger : "))

    burgers.append([code, name, price])
    return burgers


def update_burger(burgers, code):
    for burger in burgers:
        if burger[0] == code:
            new_code = input("Saisissez le nouveau code : (laissez vide si non modifié) ").lower()
            new_name = input("Saisissez le nouveau nom : (laissez vide si non modifié) ").lower()
            new_price = float(input("Saisissez le nouveau prix : (mettre 0.0 si non modifié) "))

            new_code = code if new_code == "" else new_code
            new_name = burger[1] if new_name == "" else new_name
            new_price = burger[2] if new_price == 0.0 else new_price

            burger[0] = new_code
            burger[1] = new_name
            burger[2] = new_price

    return burgers


def remove_burger(burgers, code):
    for burger in burgers:
        if burger[0] == code:
            burgers.remove(burger)

    return burgers


def check_existing_burger(burgers, code):
    result = False
    for burger in burgers:
        if burger[0] == code:
            result = True

    return result


def main():
    biburgix_menu = [
        ["ham", "le hamburger", 7.0],
        ["chb", "le cheeseburger", 7.5],
        ["bak", "le bakon burger", 7.5],
        ["bkc", "le bakon cheeseburger", 8.0],
        ["chi", "le chicken burger", 7.5],
        ["ccb", "le chicken cheeseburger", 8.0],
        ["veg", "le veggi burger", 8.0],
    ]

    choice = 0
    while choice != "99":
        show_menu()
        choice = input()

        if choice == "1":
            print(get_all_burger(biburgix_menu))

        elif choice == "2":
            biburgix_menu = create_burger(biburgix_menu)

        elif choice == "3":
            code = input("Saisissez le code du burger à modifier : ").lower()
            if check_existing_burger(biburgix_menu, code):
                biburgix_menu = update_burger(biburgix_menu, code)
            else:
                print("Le burger à modifier n'existe pas.")

        elif choice == "4":
            print(get_all_burger(biburgix_menu))

            code = input("Saisissez le code du burger à modifier : ").lower()
            if check_existing_burger(biburgix_menu, code):
                remove_burger(biburgix_menu, code)

            print(get_all_burger(biburgix_menu))

        elif choice == "99":
            print("Au revoir !")
            exit()


if __name__ == "__main__":
    main()
