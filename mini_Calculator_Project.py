while True:
    no1 = int(input("Enter your first no: "))
    no2 = int(input("Enter your second no: "))
    operator = input("Enter operator (+, -, *, /) or 'exit' to quit: ")

    if operator == "exit":
        print("Calculator exiting. Goodbye!")
        break

    if operator == "+":
        result = no1 + no2
    elif operator == "-":
        result = no1 - no2
    elif operator == "*":
        result = no1 * no2
    elif operator == "/":
        if no2 != 0:
            result = no1 / no2
        else:
            print("Error: Cannot divide by zero")
            continue
    else:
        print("Invalid Operator, please try again.")
        continue

    print(f"Result: {result}")
