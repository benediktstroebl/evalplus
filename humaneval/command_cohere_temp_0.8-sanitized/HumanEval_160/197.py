def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = []
    
    for i in range(num_operands - 1):
        if i + 1 < num_operands:
            expression.append(operand[i] * operand[i + 1])
        else:
            expression.append(operand[i])
    
    for i in range(num_operands - 2):
        operator_token = operator[i]
        if operator_token == '*':
            expression[i] = expression[i] * expression[i + 1]
        elif operator_token == '+':
            expression[i] = expression[i] + expression[i + 1]
        elif operator_token == '-':
            expression[i] = expression[i] - expression[i + 1]
        elif operator_token == '**':
            expression[i] = expression[i] ** expression[i + 1]
        else:
            expression[i] = expression[i] // expression[i + 1]
    
    return expression[-1]