def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate max times
    max_iterations = min(len(operator), len(operand)-1)
    for i in range(max_iterations):
        # For each iteration, perform the operation based on the operator and operands
        result += operand[i] * operator[i]
    # Adjust result based on the last unprocessed operand
    result += operand[-1] * operator[-1]
    return result