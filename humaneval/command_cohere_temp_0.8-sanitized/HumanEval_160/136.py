def do_algebra(operator, operand):
    result = 0
    # Calculate result using defined operations and operands
    for i in range(len(operand) - 1):
        operation = operator[i]
        a, b = operand[i], operand[i + 1]
        if operation == '+':
            result += a + b
        elif operation == '-':
            result += a - b
        elif operation == '*':
            result += a * b
        elif operation == '//':
            result += a // b
        elif operation == '**':
            result += a ** b
    return result