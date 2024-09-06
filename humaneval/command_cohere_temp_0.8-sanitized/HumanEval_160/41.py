def do_algebra(operator, operand):
    # Sort the operand list to ensure consistent ordering of elements
    operand = sorted(operand)
    
    # Construct the expression from the operator and operand lists
    expression = ' + '.join(f'{op}_{operand[i]}' for i, op in enumerate(operator))
    
    # Evaluate the expression
    result = eval(expression)
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)