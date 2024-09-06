def do_algebra(operator, operand):
    num_ops = len(operator)
    expr = []
    for i in range(num_ops):
        expr.append(operand[i] if i % 2 == 0 else operator[i] + '(' + str(operand[i]) + ')')
    return eval(' '.join(expr))