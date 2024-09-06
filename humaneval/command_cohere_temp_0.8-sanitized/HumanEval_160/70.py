def do_algebra(operator, operand):
    result = 0
    # Calculate result using the calculated expression
    for i in range(len(operand) - 1):
        result += operand[i]
        for j in range(len(operator)):
            if operator[j] == '+':
                result += operand[i + 1]
            elif operator[j] == '-':
                result -= operand[i + 1]
            elif operator[j] == '*':
                result *= operand[i + 1]
            elif operator[j] == '//':
                result //= operand[i + 1]
            elif operator[j] == '**':
                result **= operand[i + 1]
    return result