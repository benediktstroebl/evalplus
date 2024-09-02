
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
    # Write your code here

    # let's first assume that it is a bad operator
    # o = len(operator) + 1
    # op = operator[o-2]
    op = operator[-1]
    o = len(operator) - 1
    # print(f'operator = {o}, operand = {o-1}')

    if o == 0:
        return operand[0]
    else:
        if op == '+':
            return operand[0] + operand[1]
        elif op == '-':
            return operand[0] - operand[1]
        elif op == '*':
            return operand[0] * operand[1]
        elif op == '//':
            return operand[0] // operand[1]
        elif op == '**':
            return operand[0] ** operand[1]
        else:
            return operand[0]
