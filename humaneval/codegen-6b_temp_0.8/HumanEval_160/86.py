
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
    if operator == []:
        raise Exception('The operator list is empty!')
    if operand == []:
        raise Exception('The operand list is empty!')
    if len(operator) != len(operand) - 1:
        raise Exception('The length of operator list is not equal to the length of operand list minus one!')
    if all([o not in ['+', '-', '*', '//', '**'] for o in operator]):
        raise Exception('The operator list includes non-basic algebra operations!')
    if any([o not in ['+', '-', '*', '//', '**'] for o in operator]):
        raise Exception('The operand list includes non-integer values!')
    if any([o not in ['+', '-', '*', '//', '**'] for o in operator]):
        raise Exception('The operand list includes non-positive values!')

    result = operand[0]
    for i in range(1, len(operand)):
        # Addition
        if operator[i - 1] == '+':
            result += operand[i]
        # Subtraction
        elif operator[i - 1] == '-':
            result -= operand[i]
        # Multiplication
        elif operator[i - 1] == '*':
            result *= operand[i]
        # Floor division
        elif operator[i - 1] == '//':
            result //= operand[i]
        # Exponentiation
        elif operator[i - 1] == '**':
            result **= operand[i]

    return result
