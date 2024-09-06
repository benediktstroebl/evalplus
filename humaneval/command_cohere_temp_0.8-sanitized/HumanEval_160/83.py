def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators
    for i in range(len(operand) - 1):
        for j in range(len(operator)):
            result += operand[i] * eval(f'{operand[i + 1]} {operator[j]} {operand[i + 1]}')
    return result