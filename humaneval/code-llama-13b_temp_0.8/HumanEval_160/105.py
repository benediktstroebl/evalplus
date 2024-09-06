
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

    # validate input
    if ( len(operator) + 1 ) != len(operand):
        raise ValueError("Invalid length")

    for n in operand:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Invalid operand")
    
    for op in operator:
        if op not in ['+', '-', '*', '//', '**']:
            raise ValueError("Invalid operator")

    # iteratively solve the equation
    result = operand[0]
    for i, op in enumerate(operator):
        idx = i + 1
        if op == '+':
            result = result + operand[idx]
        elif op == '-':
            result = result - operand[idx]
        elif op == '*':
            result = result * operand[idx]
        elif op == '//':
            result = result // operand[idx]
        elif op == '**':
            result = result ** operand[idx]
    
    return result
