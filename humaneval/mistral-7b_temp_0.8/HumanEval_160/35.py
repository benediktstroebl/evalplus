
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
    if len(operator) != len(operand)-1:
        raise ValueError('The length of operator list is equal to the length of operand list minus one.')
    if not all(isinstance(i,int) for i in operand):
        raise ValueError('Operand is a list of of non-negative integers.')
    if len(operator) <= 0 or len(operand) <= 0:
        raise ValueError('Operator list has at least one operator, and operand list has at least two operands.')

    result = operand[0]
    for i,operation in enumerate(operator):
        if i%2 == 0:
            result = result + operand[i+1]
        else:
            result = result * operand[i+1]
        if operation == '-':
            result = result - operand[i+1]
        elif operation == '//':
            result = result // operand[i+1]
        elif operation == '**':
            result = result ** operand[i+1]
    return result
