def do_algebra(operator, operand):
    result = 0
    # Ensure proper length of operator and operand
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length must be equal to operand list length minus one.")
    # Ensure non-empty operator list
    if not operator:
        raise ValueError("Operator list must not be empty.")
    # Ensure operand is a list of integers
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand must be a list of non-negative integers.")
    # Iterate through lists to build and evaluate expression
    for i in range(len(operand) - 1):
        result += operator[i] * operand[i]
    return result