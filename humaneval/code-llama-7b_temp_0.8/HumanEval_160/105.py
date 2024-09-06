
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
    num = operand
    for op in operator:
        if op == '+':
            num = [i+j for i,j in zip(num, num[1:])]
        if op == '-':
            num = [i-j for i,j in zip(num, num[1:])]
        if op == '*':
            num = [i*j for i,j in zip(num, num[1:])]
        if op == '//':
            num = [int(i/j) for i,j in zip(num, num[1:])]
        if op == '**':
            num = [pow(i,j) for i,j in zip(num, num[1:])]
    return num[0]

