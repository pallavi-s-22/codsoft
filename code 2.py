import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length should be a positive integer.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()