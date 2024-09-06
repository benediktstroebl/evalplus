def do_algebra(operator, operand):
    # Calculate the length of the shorter list to determine the result's size.
    size = min(len(operator), len(operand)) - 1
    
    # Build and evaluate the expression.
    result = 0
    for i in range(size):
        result += operator[i] * operand[i]
    
    # Add the last operand if there is only one operator.
    if len(operator) == 1:
        result += operator[0] * operand[-1]
    
    return result