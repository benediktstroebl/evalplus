def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = []
    for i in range(num_operands):
        if i == 0:
            expression.append(operand[i])
        else:
            expression.append(operator[i-1])
            expression.append(operand[i])
    return expression[-1]