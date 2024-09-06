def do_algebra(operator, operand):
    result = 0
    # Calculate result using the declared algorithm
    for i in range(len(operand) - 1):
        result += operand[i] * eval(f'{operator[i] if i < len(operator) - 1 else "+"}' f'{{operand[i + 1] if i < len(operand) - 2 else "0"}}')
    return result