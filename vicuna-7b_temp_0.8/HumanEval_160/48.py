
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
    operand = [int(x) for x in operand]
    operator_length = len(operator)
    result = 0
    if operator_length == 1 and operand[0] == 0:
        return operand[0]
    elif operator_length == 1:
        for i in range(len(operand)):
            result = operator[0] * result + operand[i]
    else:
        for i in range(0, len(operand), operator_length):
            operator = operator[0]
            for j in range(operator_length):
                operator = operator[1]
                result += operator * operand[i]
    return result
