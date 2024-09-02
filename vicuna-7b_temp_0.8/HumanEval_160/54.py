
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
    operand = [int(op) for op in operand]
    if len(operator) > len(operand):
        raise ValueError("Operator list is longer than operand list")
    for i in range(1, len(operator)):
        if operator[i] not in ['+', '-', '*', '/']:
            raise ValueError("Operator in operator list is not a basic algebra operation")
    if not all(op >= 0 for op in operand):
        raise ValueError("Operand is not a list of non-negative integers")
    if len(operator) == 0:
        return operand[0]
    result = operator[0](*[operand[0]])
    for i in range(1, len(operator), 2):
        result = operator[i](result, operand[i-1])
    return result
