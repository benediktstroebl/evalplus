
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
    operator_list = list(operator.items())[1:]
    operands = [x[0] for x in operator_list]
    operand = [int(x) for x in operand]
    operator = [x[0] for x in operator_list]
    result = 0
    for i in range(len(operand)-1):
        result = operator[operator.index(operator.index(i)+1)][1] * operand[i] + result
    return result
