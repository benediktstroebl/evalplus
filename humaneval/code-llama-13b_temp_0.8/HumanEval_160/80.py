
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

    def do_operation(operator, array):
        if len(array) == 1:
            return array[0]
        else:
            result = None
            if operator == '+':
                result = array[0] + array[1]
            elif operator == '-':
                result = array[0] - array[1]
            elif operator == '*':
                result = array[0] * array[1]
            elif operator == '//':
                result = array[0] // array[1]
            elif operator == '**':
                result = array[0] ** array[1]
            else:
                raise ValueError('Invalid operator')
            array = [result] + array[2:]
            return do_operation(operator, array)

    return do_operation(operator, operand)
