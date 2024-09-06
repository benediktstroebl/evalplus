def do_algebra(operator, operand):
    """
    Evaluate an algebraic expression built from the given lists of operators and integers.

    Args:
        operator (list): List of basic algebra operations, such as ['+', '*', '-'].
        operand (list): List of integers, such as [2, 3, 4, 5].

    Returns:
        int: Result of the expression formed from the operator and operand lists.
    """
    # Check if the lengths of operator and operand are valid
    if len(operator) + 1 != len(operand):
        raise ValueError("Operator list should be of length 1 less than the operand list.")
        
    # Check if the operand is a list of non-negative integers
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand must be a list of non-negative integers.")
        
    # Check if the operator list has at least one element
    if not operator:
        raise ValueError("Operator list must have at least one element.")

    # Build and evaluate the expression
    expression = "".join(f'{op}{{operand[i]}}' for i, op in enumerate(operator))
    return eval(expression)