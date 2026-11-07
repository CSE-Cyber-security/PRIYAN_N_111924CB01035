import getpass
import string


def check_password_strength(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains an uppercase letter": any(c.isupper() for c in password),
        "Contains a lowercase letter": any(c.islower() for c in password),
        "Contains a number": any(c.isdigit() for c in password),
        "Contains a special character": any(c in string.punctuation for c in password),
    }

    score = sum(checks.values())

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, checks


def main():
    print("=" * 42)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 42)

    password = getpass.getpass("Enter a password: ")

    if not password:
        print("Password cannot be empty.")
        return

    strength, checks = check_password_strength(password)
    print("\nPassword Strength:", strength)
    print("\nPassword Requirements:")

    for requirement, passed in checks.items():
        result = "PASS" if passed else "FAIL"
        print(f"{result} - {requirement}")

    print("\nNote: This is a basic rule-based checker.")


if __name__ == "__main__":
    main()
