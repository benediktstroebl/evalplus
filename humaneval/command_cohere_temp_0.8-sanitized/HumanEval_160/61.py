def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate over them
    n = min(len(operator), len(operand)) - 1
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]!s}{{result}}')
    return result