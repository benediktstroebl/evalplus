
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
    # Validate the input
    if len(operator) < len(operand) - 1:
        raise ValueError('Operator list is too short')
    if not all(x >= 0 for x in operand):
        raise ValueError('Operand must contain only non-negative integers')
    # Get the operands
    a, b = operand[:-1], operand[-1]
    # Get the operator
    op = operator.pop(0)
    if op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    elif op == '**':
        result = pow(a, b)
    else:
        raise ValueError('Invalid operator')
    # Apply the operator
    result = operator[0] + str(result)
    # Get the next operator
    operator.pop(0)
    # Repeat the process
    while operator:
        op = operator.pop(0)
        if op == '+':
            result += ' + '
        elif op == '-':
            result += ' - '
        elif op == '*':
            result += ' * '
        elif op == '/':
            result += ' / '
        else:
            raise ValueError('Invalid operator')
        # Append the operator
        operator.append(op)
        # Get the next operand
        a, b = operand[:-1], operand[-1]
        # Get the next operator
        operator.pop(0)
        # Append the operand
        operator.append(a)
        # Get the next operator
        operator.pop(0)
        # Append the operand
        operator.append(b)
    # Evaluate the expression
    return eval(result)