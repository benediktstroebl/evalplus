
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
    # if the operator is not in the list, check if the operand is 0
    if operator not in list(operator.keys()):
        if operand[0] == 0:
            return 0
        else:
            return None
    else:
        # if operator is in the list, check if it is an operand
        if operator in operand:
            return operand[operator]
        else:
            # get the index of the operator in the operand list
            index = operand.index(operator)
            # use the basic algebra operations to calculate the result
            result = 0
            if index % 2 == 0:
                result = (operand[index//2] ** (index//2))
            else:
                result = (operand[index//2] ** (index//2) - operand[index//2-1])
            return result
