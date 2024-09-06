def do_algebra(operator, operand):
    num_operands = len(operand)
    expr_str = ' '.join([f'{op} {operand[i]}' for i, op in enumerate(operator)])
    return eval(expr_str)