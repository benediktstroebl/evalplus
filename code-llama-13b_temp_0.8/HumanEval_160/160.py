
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

    # length of operator list == length of operand list - 1
    assert len(operator) == len(operand) - 1

    # define expression as an empty string
    expression = ''
    # iterate through operand list
    for i in range(len(operand)):
        # if i is equal to zero, set expression as str(operand[i])
        if i == 0:
            expression += str(operand[i])
        # otherwise
        else:
            # add operator[i-1] + str(operand[i]) to expression
            expression += operator[i-1] + str(operand[i])
    # evaluate expression and return result
    return eval(expression)

