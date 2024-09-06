def do_algebra(operator, operand):
    result = 0
    operands = len(operand)
    for i in range(operands - 1):
        result += operand[i] * operator.index(operator[i])
        if operator[i] == '*':
            result //= operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '**':
            result = result * operand[i + 1]
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]