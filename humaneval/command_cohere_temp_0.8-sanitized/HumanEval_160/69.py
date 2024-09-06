def do_algebra(operator, operand):
    """
    Build an algebraic expression using the provided operator and operand lists and return its evaluation.
    """
    # Ensure consistent lengths of operator and operand
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lists must have equal length.")
    
    # Use concatenation to build the expression from tokens
    expression = ' '.join([f'{op}_{operand[i]}' for i, op in enumerate(operator)])
    
    # Evaluate the expression using Python's eval() function
    return eval(expression)