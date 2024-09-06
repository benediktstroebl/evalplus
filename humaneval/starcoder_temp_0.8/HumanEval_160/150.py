
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
    import operator as op
    if len(operator)!= len(operand) - 1:
        raise ValueError("Length of operator list should be equal to the length of operand list minus one.")
    for o in operator:
        if o not in ['+', '-', '*', '//', '**']:
            raise ValueError("Operator can only be one of '+', '-', '*', '//', '**'.")
    expression = ''
    for i,o in enumerate(operator):
        expression += f"operand[{i}]"
        expression += o
        expression += "operand["
        expression += str(i + 1)
        expression += "]"
    expression += f"operand[{len(operator)}]"
    return eval(expression)
