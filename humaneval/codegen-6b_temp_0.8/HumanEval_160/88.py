
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
    def _eval(operator, operand, i):
        if i == len(operand):
            return int(operator[0] == '+' or operator[0] == '-' or operator[0] == '*')
        else:
            return int(operator[0] == '+' and _eval(operator[1:], operand, i + 1)) + int(
                operator[0] == '-' and _eval(operator[1:], operand, i + 1)) * int(
                operator[0] == '*' and _eval(operator[1:], operand, i + 1))

    return _eval(operator, operand, 0)

