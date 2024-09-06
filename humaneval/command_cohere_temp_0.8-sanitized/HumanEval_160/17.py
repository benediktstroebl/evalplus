def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = ''
    
    for i in range(num_operands):
        if i > 0: 
            expression += ' ' + operator[i-1] + ' '
        expression += str(operand[i])
    
    return eval(expression)