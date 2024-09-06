def do_algebra(operator, operand):
    num_operands = len(operand)
    expr_lines = []
    for i in range(num_operands - 1):
        expr_lines.append(f'{operand[i] } {operator[i]} {operand[i + 1]}')
    expr = ' '.join(expr_lines)
    return eval(expr)