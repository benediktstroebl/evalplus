def do_algebra(operator, operand):
    result = 0
    # Calculate result using the defined algebra operations and operands
    for i in range(len(operand) - 1):
        result += operand[i] * eval(f'{operator[i]!s}{operand[i+1]!s}')
    return result