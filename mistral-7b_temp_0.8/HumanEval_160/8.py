
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
    # first we need to find the length of the operator list
    length_of_operator = len(operator)
    # we then have to add 1 to this length
    length_of_operator += 1
    # this is because we need to split the array into 2 parts, the first part is for the
    # multiplication (operator list) and the second part is for the addition (operand list)
    multi_part = operator[:length_of_operator]
    # once we have this split, we can now apply the formula from the above problem
    result = 0
    # we need to iterate through the list
    for x in range(0, len(multi_part)):
        # we then need to apply the formula
        result = result * operand[x]
    return result
