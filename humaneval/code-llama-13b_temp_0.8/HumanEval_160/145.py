
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
    # add a 'dummy' value to the operator list
    # so that we can get the 'next operator'
    operand.insert(0,0)
    result = operand[0]
    op = '+'
    for i in range(1, len(operator)+1):
        if op == '+':
            result += operand[i]
        elif op == '-':
            result -= operand[i]
        elif op == '*':
            result *= operand[i]
        elif op == '//':
            result //= operand[i]
        elif op == '**':
            result **= operand[i]
        op = operator[i-1]
    return result
