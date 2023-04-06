def basic_calculator():
    """
    This function implements a basic calculator.
    It takes two numbers as input and performs basicss operations on them.
    """
    # Get two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform basic arithmetic operations
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter choice (1/2/3/4): "))

    if choice == 1:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == 4:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")