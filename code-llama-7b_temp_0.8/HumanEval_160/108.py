
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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    if len(operator) != len(operand) - 1:
        return None
    if len(operator) == 0:
        return operand[0]

    for idx in range(len(operator)):
        operand[idx + 1] = eval(f'{operand[idx]} {operator[idx]} {operand[idx + 1]}')
    return operand[-1]

