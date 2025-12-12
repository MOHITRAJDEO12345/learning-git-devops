def get_operation():
    operations = {"add", "mul", "sub", "div"}
    while True:
        choice = input("Choose operation (add/mul/sub/div): ").strip().lower()
        if choice in operations:
            return choice
        print("Invalid choice. Try again.")


def get_numbers_for_add_mul(operation):
    prompt = "Enter numbers separated by spaces: "
    while True:
        parts = input(prompt).strip().split()
        if len(parts) < 2:
            print("Provide at least two numbers.")
            continue
        try:
            numbers = [float(p) for p in parts]
            return numbers
        except ValueError:
            print("Non-numeric value detected. Try again.")


def get_two_numbers(operation):
    prompt = "Enter two numbers separated by space: "
    while True:
        parts = input(prompt).strip().split()
        if len(parts) != 2:
            print("Provide exactly two numbers.")
            continue
        try:
            return float(parts[0]), float(parts[1])
        except ValueError:
            print("Non-numeric value detected. Try again.")


def add(numbers):
    return sum(numbers)


def multiply(numbers):
    result = 1.0
    for num in numbers:
        result *= num
    return result


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main():
    operation = get_operation()
    try:
        if operation in {"add", "mul"}:
            numbers = get_numbers_for_add_mul(operation)
            result = add(numbers) if operation == "add" else multiply(numbers)
        else:
            a, b = get_two_numbers(operation)
            result = subtract(a, b) if operation == "sub" else divide(a, b)
        print(f"Result: {result}")
    except ZeroDivisionError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()