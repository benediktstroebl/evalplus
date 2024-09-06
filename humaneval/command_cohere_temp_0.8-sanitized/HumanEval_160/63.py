def do_algebra(operator, operand):
    result = 0
    for i in range(len(operand) - 1):
        result += operator[i] * operand[i+1]
    return result