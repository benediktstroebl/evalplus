def do_algebra(operator, operand):
    # type the expression
    expression = ' '.join([f'{o}{{operand[i]}}' for i, o in enumerate(operator)])
    
    # evaluate the expression
    result = eval(expression)
    
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]