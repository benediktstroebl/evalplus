def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
        for j in range(i + 1, num_operands):
            operator_str = operator[j - i - 1]
            if operator_str == '+':
                expr.append(expr[i] + expr[j])
            elif operator_str == '-':
                expr.append(expr[i] - expr[j])
            elif operator_str == '*':
                expr.append(expr[i] * expr[j])
            elif operator_str == '//':
                expr.append(expr[i] // expr[j])
            elif operator_str == '**':
                expr.append(expr[i] ** expr[j])
    return expr[-1]