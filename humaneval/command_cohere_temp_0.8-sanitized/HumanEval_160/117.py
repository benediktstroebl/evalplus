def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = ""
    
    # Ensure that the maximum number of operands is used.
    # If the length of operator list is less than the length of operand list, 
    # extend the operator list with '*' so the length of the two lists is the same.
    if len(operator) < num_operands:
        operator += ['*'] * (num_operands - len(operator))

    for i in range(num_operands - 1):
        expression += str(operand[i]) + ' ' + operator[i] + ' '

    # Add the last operand to the expression without a separator
    expression += str(operand[-1])
    
    return eval(expression)
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]