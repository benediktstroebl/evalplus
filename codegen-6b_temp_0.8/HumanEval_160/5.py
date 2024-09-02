
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
    if len(operator) == 0:
        return operand[0]
    if len(operand) == 1:
        return operand[0]
    if operator[0] == '+':
        return do_algebra('*', [operator[1], operator[2], operand[0]]) + do_algebra('+', [operator[1], operator[2], operand[1]])
    if operator[0] == '-':
        return do_algebra('*', [operator[1], operator[2], operand[0]]) - do_algebra('+', [operator[1], operator[2], operand[1]])
    if operator[0] == '*':
        return do_algebra('+', [operator[1], operator[2], do_algebra('*', [operator[1], operator[2], operand[0]])]) * do_algebra('+', [operator[1], operator[2], operand[1]])
    if operator[0] == '//':
        return do_algebra('+', [operator[1], operator[2], do_algebra('/', [operator[1], operator[2], operand[1]])]) // do_algebra('+', [operator[1], operator[2], operand[0]])
    if operator[0] == '**':
        return do_algebra('*', [operator[1], operator[2], do_algebra('**', [operator[1], operator[2], operand[0]])]) ** do_algebra('+', [operator[1], operator[2], operand[1]])
    
    return do_algebra(operator[0], [operator[1], operator[2], operand[0]])
    
assert(do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 0)
assert(do_algebra(['+', '+'], [2, 3, 4, 5]) == 8)
assert(do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == -1)
assert(do_algebra(['*', '*