def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to loop through
    n = min(len(operator), len(operand)) - 1
    # Checking if the lists are empty
    if n < 0:
        return "Error: the given lists are empty, please provide valid lists"

    # Looping through the lists to build and evaluate the expression
    for i in range(n):
        result += operand[i]
        for j in range(len(operand)-i-1):
            result += operator[j] * operand[i+j+1]
    return result