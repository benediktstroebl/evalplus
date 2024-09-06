
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
    stack = []
    for i, operand in enumerate(operator):
        if operand == '*':
            stack.append(operand)
        elif operand == '//':
            stack.append(operand)
        elif operand == '**':
            stack.append(operand)
        else:
            if i == len(operator) - 1:
                stack.append(operand)
            else:
                stack.append(operand)
    stack.append(operand)
    for i, operand in enumerate(operator):
        if i != len(operator) - 1:
            stack.append(operand)
            if i != 0:
                stack.append(operand)
            else:
                stack.append(operand)
    return sum(int(x) for x in stack)
