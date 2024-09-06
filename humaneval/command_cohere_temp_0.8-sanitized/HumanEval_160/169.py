def do_algebra(operator, operand):
    result = 0
    for i in range(len(operand) - 1):
        result += operand[i] * eval(f'{operator[i] if i < len(operator) - 1 else "+"}.join(operand[i+1:])')
    return result