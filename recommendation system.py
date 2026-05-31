print("    MOVIE RECOMMENDATION SYSTEM")

while True:

    print("\nAvailable Genres:")
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")
    print("4. Romance")
    print("5. Sci-Fi")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nRecommended Action Movies:")
        print("- Avengers")
        print("- Batman")
        print("- John Wick")

    elif choice == "2":
        print("\nRecommended Comedy Movies:")
        print("- Mr. Bean")
        print("- The Mask")
        print("- Home Alone")

    elif choice == "3":
        print("\nRecommended Horror Movies:")
        print("- Conjuring")
        print("- Annabelle")
        print("- IT")

    elif choice == "4":
        print("\nRecommended Romance Movies:")
        print("- Titanic")
        print("- The Notebook")
        print("- La La Land")

    elif choice == "5":
        print("\nRecommended Sci-Fi Movies:")
        print("- Interstellar")
        print("- Inception")
        print("- Avatar")

    elif choice == "6":
        print("\nThank you for using the recommendation system!")
        break

    else:
        print("\nInvalid choice! Please try again.")