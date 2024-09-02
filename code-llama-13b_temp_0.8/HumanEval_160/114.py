
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
    # calculate the result recursively
    # simple cases:
    if len(operand) == 1:
        return operand[0]
    elif len(operand) == 2:
        # add operator in between operand:
        return eval(str(operand[0]) + operator[0] + str(operand[1]))
    
    if len(operand) > 2:
        # add operator between operand[0] and operand[1]:
        result = eval(str(operand[0]) + operator[0] + str(operand[1]))
        # recursive call:
        return do_algebra(operator[1:], operand[1:])


