import json


def filter_users_by_name(name):
    """Return users whose name matches the given value (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)
    return [user for user in users if user["name"].lower() == name.lower()]


def filter_users_by_age(age):
    """Return users whose age matches the given value."""
    with open("users.json", "r") as file:
        users = json.load(file)
    return [user for user in users if user["age"] == age]


def filter_users_by_email(email):
    """Return users whose email matches the given value (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)
    return [user for user in users if user["email"].lower() == email.lower()]


def main():
    """Main function to handle user input and display filtered users."""
    filter_option = input(
        "What would you like to filter by? (name, age, email): "
    ).strip().lower()

    if filter_option == "name":
        name = input("Enter a name to filter users: ").strip()
        filtered_users = filter_users_by_name(name)

    elif filter_option == "age":
        while True:
            try:
                age = int(input("Enter an age to filter users: "))
                filtered_users = filter_users_by_age(age)
                break
            except ValueError:
                print("Please enter a valid age.")

    elif filter_option == "email":
        email = input("Enter an email to filter users: ").strip()
        filtered_users = filter_users_by_email(email)

    else:
        print("Filtering by that option is not supported.")
        return

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found with that filter.")


if __name__ == "__main__":
    main()