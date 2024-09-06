def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to subtract it from the length of the longer list
    length_to_sub = min(len(operator), len(operand)) - 1
    for i in range(length_to_sub):
        result += operand[i]  # Add the operand to the result
        operator = operator[i] + operator[0]  # Concatenate the current operator with the next operator
    result += int(operator)  # Add the last operator as an integer to the result
    return result