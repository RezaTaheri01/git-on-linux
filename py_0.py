def welcome(name: str):
    return f"Welcome {name.capitalize()}"


if __name__ == "__main__":
    result = welcome(input("Your name:"))
    print(result)
