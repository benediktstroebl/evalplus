def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
    for i in range(num_operands - 1):
        expr.append(operator[i])
    expr.pop()
    return eval(' '.join(map(str, expr)))