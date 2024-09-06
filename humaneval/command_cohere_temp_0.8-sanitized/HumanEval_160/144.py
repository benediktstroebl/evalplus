def do_algebra(operator, operand):
    result = 0
    # Calculate result using predefined expressions
    for i in range(len(operand)-1):
        # Use the eval function to evaluate the expression in the operator string
        # The expression = operand[0] + ... + operand[i] + ... + operand[n]
        result += eval(str(operand[0]) + operator[0] + ''.join(str(x) for x in operand[1:i]) + 
                           operator[1] + ''.join(str(x) for x in operand[i+1:]))
    return result