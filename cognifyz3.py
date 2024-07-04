import re

def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

    # Compile the pattern into a regex object
    regex = re.compile(pattern)

    # Check if the email matches the pattern
    if regex.match(email):
        return True
    else:
        return False

if __name__ == "__main__":
    # Example usage:
    email = input("Enter an email address to validate: ")
    if validate_email(email):
        print(f"The email address '{email}' is valid.")
    else:
        print(f"The email address '{email}' is not valid.")
