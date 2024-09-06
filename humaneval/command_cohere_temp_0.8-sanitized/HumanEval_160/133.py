def do_algebra(operator, operand):
    result = 0
    # Compute the result using simple sequential operations
    for i in range(len(operand)):
        for j in range(len(operator)):
            if operator[j] == '+':
                result += operand[i]
            elif operator[j] == '-':
                result -= operand[i]
            elif operator[j] == '*':
                result *= operand[i]
            elif operator[j] == '//':
                result //= operand[i]
            elif operator[j] == '**':
                result **= operand[i]
    return result