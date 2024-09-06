def do_algebra(operator, operand):
    result = 0
    # Calculate result using the reduced operators list
    for i in range(len(operand) - 1):
        result += operand[i] * operand[i+1]
        for j in range(len(operator)):
            if operator[j] == '+':
                result += operand[i+1]
            elif operator[j] == '-':
                result -= operand[i+1]
            elif operator[j] == '*':
                result *= operand[i+1]
            elif operator[j] == '//':
                result //= operand[i+1]
            elif operator[j] == '**':
                result **= operand[i+1]
    return result