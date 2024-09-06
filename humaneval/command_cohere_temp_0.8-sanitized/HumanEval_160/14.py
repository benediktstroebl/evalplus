def do_algebra(operator, operand):
    result = 0
    # iterate over the operand list and use the corresponding operator to calculate the expression
    for i in range(len(operand)):
        result += operand[i] * eval(f'{operator[i]}{{operand[i+1]}}')
    return result