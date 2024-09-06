
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

    result = 0

    if len(operator) == 0:
        return 0
    elif len(operator) == 1:
        return operand[0]

    while len(operator) > 1:
        operand_left = operand.pop(0)
        operand_right = operand.pop(0)

        if operator[0] == '+':
            operand.insert(0, operand_left + operand_right)
        elif operator[0] == '-':
            operand.insert(0, operand_left - operand_right)
        elif operator[0] == '*':
            operand.insert(0, operand_left * operand_right)
        elif operator[0] == '//':
            operand.insert(0, operand_left // operand_right)
        elif operator[0] == '**':
            operand.insert(0, operand_left ** operand_right)

        operator.pop(0)

    if len(operand) == 1:
        result = operand[0]
    return result
