def main():
    tasks = []

#käyttäjä valistee valintansa

while True:
    print("\n==== Tehtävä Lista ====")
    print("1. Lisää Tehtävä")
    print("2. Näytä Tehtävät")
    print("3. Merkitse tehtävä tehdyksi")
    print("4. Poistu")

    choice = input("Lisää valintasi: ")

#jos käyttäjä valitsee 1. valinnan, käyttäjä päsee lisäämään tehtäviä

    if choice == '1':
        print()
        n_tasks = int(input("Kuinka monta tehtävää haluat lisätä: "))

        for i in range(n_tasks):
            task = input("Lisää tehtävä: ")
            task.append({"Tehtävä": task, "valmis": False})
            print("Tehtävä lisätty!")
    
#jos käyttäjä valitsee 2. valinnan, käyttäjä näkee tehdyt ja tekemättömät tehtävät

    elif choice == '2':
        print("\nTasks:")
        for index, task in enumerate(task):
            status = "Valmis" if task["valmis"] else "Ei Valmis"
            print(f"{index + 1}. {task['task']} - {status}")

#jos käyttäjä valitsee 3. valinnan, käyttäjä pystyy merkkaamaan tehtävän valmiiksi

    elif choice == '3':
        task_index = int(input("merkkaa tehtävä numero tehdyksi: ")) - 1
        if 0 <= task_index < len(task):
            task[task_index]["valmis"] = True
            print("tehtävä tehty!")
        else:
            print("virheellinen tehtävä numero.")

#

    elif choice == '4':
        print("Poistutaan tehtävät listalta...")
        break

    else:
        print("Virheellinen valinta. Yritä uudelleen.")