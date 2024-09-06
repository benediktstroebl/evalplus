def do_algebra(operator, operand):
    num_ops = len(operator)
    expr = []
    for i in range(num_ops):
        expr.append(operand[i])
        for j in range(i+1, num_ops):
            expr.append(operator[i] + operator[j])
    return expr[-1]