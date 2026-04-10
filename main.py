import random
import string


def get_length():

    while True:
        try:
            length = int(input("Enter password length: "))

            if length <= 0:
                print("Length must be positive.")
                continue

            return length

        except ValueError:
            print("Please enter a valid number.")


def build_character_pool():

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    return all_characters


def generate_password(length, characters):

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():

    print("Password Generator")
    print("------------------")

    length = get_length()

    characters = build_character_pool()

    password = generate_password(length, characters)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
