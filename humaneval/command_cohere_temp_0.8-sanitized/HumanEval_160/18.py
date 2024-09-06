import unittest
def do_algebra(operator, operand):
    num_ops = len(operator)
    expr = []
    for i in range(num_ops):
        expr.append(operand[i])
        for j in range(i + 1, len(operand)):
            expr.append(operator[i] + ' ' + operand[j])
    return eval(expr[0])(*expr[1:])