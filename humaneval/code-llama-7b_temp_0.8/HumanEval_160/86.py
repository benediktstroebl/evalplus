
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
    # Calculation using stack
    stack = []
    for operand in operand:
        stack.append(operand)
    while len(operator) > 0:
        # do calculation
        if operator.pop() == '+':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 + v2)
        elif operator.pop() == '-':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 - v2)
        elif operator.pop() == '*':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 * v2)
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 // v2)
    return stack.pop()


