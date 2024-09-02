
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
    # check that the operator list and operand list have the correct length
    if len(operator) != len(operand) - 1:
        return -1
    
    # check that the operator is an arithmetic operator
    if operator not in ['+', '-', '*', '/', '//']:
        return -1
    
    # check that the operand is a list of non-negative integers
    if not isinstance(operand, list) or not all(map(int, operand)) or any(operand < 0):
        return -1
    
    # check that the operator is greater than the first operand
    if operator[0] != operand[0]:
        return -1
    
    # perform the operation
    result = operand[operator.index(operand[0])]
    
    # check that the operator is greater than the second operand
    if operator[1] != operand[1]:
        return -1
    
    # perform the operation
    result = operator[1](result, operand[operator.index(operator[1])])
    
    return result
