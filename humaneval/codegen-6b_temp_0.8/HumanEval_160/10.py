
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
    n = len(operator)

    def do_basic_algebra(operator, operand):
        n = len(operator)
        if n == 0:
            return None
        operator0 = operator[0]
        operator1 = operator[1:]
        operand0 = operand[:len(operand) - 1]
        operand1 = operand[1:]

        if operator0 == '+':
            operand0.insert(0, 0)
            return do_basic_algebra(operator1, operand0) + do_basic_algebra(operator1, operand1)
        elif operator0 == '*':
            return do_basic_algebra(operator1, operand0) * do_basic_algebra(operator1, operand1)
        elif operator0 == '-':
            operand0[0] = - operand0[0]
            return do_basic_algebra(operator1, operand0) - do_basic_algebra(operator1, operand1)
        elif operator0 == '//':
            return do_basic_algebra(operator1, operand0) // do_basic_algebra(operator1, operand1)
        elif operator0 == '**':
            return do_basic_algebra(operator1, operand0) ** do_basic_algebra(operator1, operand1)
        else:
            return None

    return do_basic_algebra(operator, operand)

