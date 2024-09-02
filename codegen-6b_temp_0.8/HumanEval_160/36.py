
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
    operator_indices = range(len(operator))
    for i in operator_indices:
        if i < len(operator):
            operator[i] = operator[i] + '+'
    operator = operator + '+'

    for i in operator_indices:
        if i < len(operator):
            del operator[i]

    for i in operator_indices:
        for j in operator_indices:
            if i < len(operator) and j < len(operator):
                operator[i] = operator[i] + '*'

    for i in operator_indices:
        if i < len(operator):
            del operator[i]

    for i in operator_indices:
        operator[i] = operator[i] + '-'

    for i in operator_indices:
        if i < len(operator):
            del operator[i]

    for i in operator_indices:
        operator[i] = operator[i] + '*'

    for i in operator_indices:
        if i < len(operator):
            del operator[i]

    for i in operator_indices:
        operator[i] = operator[i] + '//'

    for i in operator_indices:
        if i < len(operator):
            del operator[i]

    for i in operator_indices:
        operator[i] = operator[i] + '**'

    for i in operator_indices:
        if i < len(operator):
            del operator[i]

    try:
        if len(operand) == 2:
            for i in operator_indices:
                if i < len(operator):
                    operator[i] = int(operator[i])
            for i in operator_indices:
                if i < len(operator):
                    operand[i] = int(operand[i])
            result = operator[0] + operator[1] + operand[0] + int(operand[1])
            return result
    except:
        return "Error. Please enter valid inputs."
