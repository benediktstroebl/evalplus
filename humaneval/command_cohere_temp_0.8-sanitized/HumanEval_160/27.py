def do_algebra(operator, operand):
    result = 0
    # Use the same length for operator and operand for a simple loop
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i]
        elif operator[i] == '-':
            result -= operand[i]
        elif operator[i] == '*':
            result *= operand[i]
        elif operator[i] == '//':
            result //= operand[i]
        elif operator[i] == '**':
            result **= operand[i]
    return result