def do_algebra(operator, operand):
    result = 0
    # Ensure that the lengths of operator and operand are compatible for proper calculations
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lengths must be compatible!")
    # Ensure we have an operator and sufficient operands
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Operator list must have at least one operator and operand list must have at least two operands!")
    # Loop through the operators and operands, building up the expression and evaluating it
    for i in range(0, len(operand)):
        if i > 0:
            result += operator[i-1] * operand[i]
        else:
            result += operand[i]
    return result