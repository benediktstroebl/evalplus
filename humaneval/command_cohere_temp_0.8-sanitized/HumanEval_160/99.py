def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate over it twice
    n = min(len(operator), len(operand))
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{result}')
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]