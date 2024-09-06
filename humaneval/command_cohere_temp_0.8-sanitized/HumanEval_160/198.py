def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate 3 times
    n = min(len(operator), len(operand))
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{{result}}')
    return result