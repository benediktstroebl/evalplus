
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

    assert operator and operand
    assert isinstance(operand, list)
    assert isinstance(operator, list)

    # Simple case with only one operand
    if len(operand) == 1:
        return operand[0]

    # Operator with two operands
    if len(operand) == 2:
        return eval("operand[0] " + operator[0] + " operand[1]")

    # Operator with more than two operands
    if len(operand) > 2:
        tmp = [operand[0]]
        for i in range(len(operator)):
            tmp.append(operator[i])
            tmp.append(operand[i + 1])
        return do_algebra(tmp[0::2], tmp[1::2])

