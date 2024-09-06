def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly, as it needs to be iterated through differently
    exp_op = operator.count('**')
    if exp_op > 0:
        for i in range(len(operand) - 1):
            result += operand[i] ** operand[i + 1]
    else:
        for i in range(len(operand) - 1):
            if operator[i] == '+':
                result += operand[i] + operand[i + 1]
            elif operator[i] == '-':
                result += operand[i] - operand[i + 1]
            elif operator[i] == '*':
                result += operand[i] * operand[i + 1]
            else:  # // case
                result += operand[i] // operand[i + 1]
    return result