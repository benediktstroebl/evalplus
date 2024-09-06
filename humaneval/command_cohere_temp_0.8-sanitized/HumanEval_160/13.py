def do_algebra(operator, operand):
    num_ops = len(operator)
    expr = []
    for i in range(num_ops):
        expr.append(operand[i])
        for j in range(i+1, len(operand)):
            expr.append(operator[i] + str(operand[j]))
    return eval(expr[0] + ' '*num_ops + expr[num_ops])