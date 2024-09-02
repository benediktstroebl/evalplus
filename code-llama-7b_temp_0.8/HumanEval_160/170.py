
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
    # your code here
    if len(operator) != len(operand) - 1:
        return 'wrong length'

    # to avoid the case of empty list
    if len(operator) == 0:
        return operand

    temp = []
    for i in range(len(operator)):
        op1 = operand[i]
        op2 = operand[i+1]
        temp.append(eval(str(op1) + operator[i] + str(op2)))

    return do_algebra(operator[:-1], temp)

