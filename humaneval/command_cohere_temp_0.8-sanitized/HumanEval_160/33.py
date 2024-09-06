def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
    expr.append(1)

    for i in range(num_operands - 1):
        expr[i+1] = expr[i+1] * (-1) if operator[i] == '-' else expr[i+1] * operand[i]
        expr[i+1] = expr[i] + expr[i+1] if operator[i] == '+' else expr[i] - expr[i+1]
        expr[i+1] = expr[i] * expr[i+1] if operator[i] == '*' else expr[i] // expr[i+1]
        expr[i+1] = expr[i] ** expr[i+1] if operator[i] == '**' else expr[i+1] ** expr[i]

    return expr[-1]
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]