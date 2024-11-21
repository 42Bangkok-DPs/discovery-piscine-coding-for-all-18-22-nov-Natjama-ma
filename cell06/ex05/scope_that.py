def add_one(x):
    x += 1
    return x

if __name__ == "__main__":
    number = 5
    print(f"Before calling add_one: {number}")

    number = add_one(number)
    print(f"After calling add_one: {number}")
