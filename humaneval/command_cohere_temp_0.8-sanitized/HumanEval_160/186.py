def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression using the provided operator and operand.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lists must have matching lengths.")
    
    expression = []
    for i in range(len(operand) - 1):
        expression.append(operand[i])
        for j in range(len(operator)):
            if operator[j] == '+':
                expression.append(expression[-1] + expression[-2])
                expression.pop()
            elif operator[j] == '-':
                expression.append(expression[-1] - expression[-2])
                expression.pop()
            elif operator[j] == '*':
                expression.append(expression[-1] * expression[-2])
                expression.pop()
            elif operator[j] == '**':
                expression.append(expression[-1] ** expression[-2])
                expression.pop()
            elif operator[j] == '/':
                if expression[-1] == expression[-2] == 0:
                    raise ValueError("Division by zero is not allowed.")
                expression.append(expression[-1] // expression[-2])
                expression.pop()
            else:
                raise ValueError(f"Invalid operator: {operator[j]}")
    
    return expression[-1]
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]