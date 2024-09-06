def do_algebra(operator, operand):
    result = 0
    # Calculate result using the parsed expression
    for i in range(len(operand) - 1):
        current_operator = operator[i]
        # Uncomment below to trace the code
        # print(f"Processing operator: {current_operator}, Operand: {operand[i]}, Result: {result}")
        result = result + operand[i]
        if current_operator == '+':
            result = result + operand[i + 1]
        elif current_operator == '-':
            result = result - operand[i + 1]
        elif current_operator == '*':
            result = result * operand[i + 1]
        elif current_operator == '//':
            result = result // operand[i + 1]
        elif current_operator == '**':
            result = result ** operand[i + 1]
    return result