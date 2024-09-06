def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
    for i in range(num_operands - 1):
        ope = operator[i]
        if i != num_operands - 2:
            expr.append(ope)
            expr.append(operand[i + 1])
    return expr[0](*expr[1:])