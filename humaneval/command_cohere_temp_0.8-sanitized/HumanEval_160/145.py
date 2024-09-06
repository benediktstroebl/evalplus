def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression using two input lists: operator and operand. 
    The returned value of the expression is computed based on the provided operands and algebra operations in the operator list.
    
    Parameters:
    - operator (list): List of basic algebra operations, including '+' for addition, '-' for subtraction, '*' for multiplication, 
    '//' for floor division, and '**' for exponentiation.

    - operand (list): List of integers used as operands in the algebraic expression.

    Returns:
    - int: Result of the algebraic expression created using the operands and the provided operator list.

    """
    # Check if the lengths of operator and operand lists are compatible for building an expression
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length must be equal to the length of operand list minus one.")

    # Iterate through the operator list and build the expression
    expression = ""
    for oper in operator:
        if expression:
            expression += " " + oper
        else:
            expression = oper

    # Evaluate the expression using the operands
    result = eval(expression, {"__builtins__": None}, {"%": lambda x, y: x // y, "**": lambda x, y: x ** y})
    
    return result