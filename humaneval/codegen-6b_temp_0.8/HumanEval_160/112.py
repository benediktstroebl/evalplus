
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
    # NOT NEEDED :-D 
    if len(operator) == 1:
        return operator[0]

    min_length = min(len(operator), len(operand))
    operator, operand = operator[:min_length], operand[:min_length]
    result = operator[0]

    max_power = len(operator) - 1

    def _algebra(operator, operand, result, power):
        operator, operand = operator[1:], operand[1:]
        if len(operator) > 0:
            result = operator[0]
            return _algebra(operator, operand, result, power + 1)
        raise
        return result ** power

    return _algebra(operator, operand, result, 0)


