def do_algebra(operator, operand):
    result = 0
    # Calculate result using binary right evaluation
    for i in range(len(operand) - 1):
        # Calculate the current element in the expression
        element_result = operand[i] + operator[i] * operand[i + 1]
        # Update the result with the latest evaluated expression
        result += element_result
    return result