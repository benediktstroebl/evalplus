def do_algebra(operator, operand):
    num_operands = len(operand)
    expression_list = []
    for i in range(num_operands):
        expression = []
        for sign in operator:
            if sign == '+':
                expression.append(operand[i])
            elif sign == '-':
                expression.append(-operand[i])
            elif sign == '*':
                expression.append(expression[-1] * operand[i])
            elif sign == '**':
                expression.append(expression[-1] ** operand[i])
            elif sign == '/':
                expression.append(expression[-1] // operand[i])
        expression_list.append(''.join(map(str, expression)))
    return eval(' '.join(expression_list))