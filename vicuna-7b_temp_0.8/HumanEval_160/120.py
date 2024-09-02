
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # Check the length of operator and operand lists
    if len(operator) != len(operand) - 1:
        raise ValueError('The length of operator list is not correct')
    if not any(isinstance(op, (int, float)) for op in operator):
        raise ValueError('Operator must be a basic algebra operation')
    
    # Get the operands
    left = operand[0]
    right = operand[1]
    # Get the operator
    operator = operator[0]
    
    # Evaluate the expression
    result = operator(left, right)
    
    # Return the result
    return result
