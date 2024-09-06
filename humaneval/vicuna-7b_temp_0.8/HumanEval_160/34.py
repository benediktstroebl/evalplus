
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
    # Check if the lists have the same length
    if len(operator) != len(operand) - 1:
        raise ValueError('The length of operator list must be equal to the length of operand list minus one')

    # Get the operator and operand
    op = operator.pop(0)
    operand_vals = operand
    
    # Get the operands
    left = operand_vals[0]
    right = operand_vals[1]
    # Evaluate the expression
    val = 0
    for val in operand_vals[2:]:
        val = op(left, val)
    # Return the evaluation
    return val
