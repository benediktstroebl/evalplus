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
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list should be equal to the length of operand list minus one.")

    expr = str(operand[0])
    for i in range(1, len(operand)):
        op = operator[i-1]
        num = operand[i]
        if op == '+':
            expr += f' + {num}'
        elif op == '-':
            expr += f' - {num}'
        elif op == '*':
            expr += f' * {num}'
        elif op == '//':
            expr += f' // {num}'
        elif op == '**':
            expr += f' ** {num}'
        else:
            raise ValueError("Invalid operator.")

    return eval(expr)
