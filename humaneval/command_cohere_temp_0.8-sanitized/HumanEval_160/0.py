def do_algebra(operator, operand):
    """
    Evaluate an algebraic expression using predefined operators and a list of operands.

    Args:
        operator (list): List of strings representing algebraic operations, such as '+', '-', '*', '/', '**'.
        operand (list): List of integers serving as the operands for the operations.

    Returns:
        int: Result of the evaluated algebraic expression based on the given operator and operand.

    Example:
        >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
        9
    """
    # Ensure the lengths of operator and operand are consistent
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length must match operand list length minus one.")

    # Iteratively build the expression and evaluate
    expression = ""
    for i in range(len(operand) - 1):
        expression += f"{operand[i]}"
        expression += f" {operator[i]}"
        if i != len(operand) - 2:
            expression += " "

    return eval(expression)