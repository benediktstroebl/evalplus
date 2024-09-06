import ast
def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands):
        if i != 0:
            expr.append(operator[i-1])
        expr.append(operand[i])
    return ast.literal_eval(' '.join(expr))