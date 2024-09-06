def do_algebra(operator, operand):
    expr = ''
    for i in range(len(operand) - 1):
        if i > 0:
            expr += ' ' + operator[i-1]
        expr += f'{operand[i]}{operand[i+1]}'
    return eval(expr)