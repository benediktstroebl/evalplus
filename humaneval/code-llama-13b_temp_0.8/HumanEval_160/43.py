
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
    # get the first operator and two operands
    idx = 0
    while idx < len(operand):
        # perform the operation
        operator_func = operator_func_dict[operator[0]]
        operand[idx] = operator_func(operand[idx], operand[idx+1])
        # delete the second operand
        del operand[idx+1]
        # if there is a next operator
        if idx < len(operator):
            # get the next operator
            operator_func = operator_func_dict[operator[idx]]
            # get the first operand
            operand[idx] = operator_func(operand[idx], operand[idx+1])
            # delete the second operand
            del operand[idx+1]
        # delete the first operator
        del operator[0]
        # increment the index
        idx += 1
    # return the first operand
    return operand[0]

    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '//': lambda x, y: x // y,
    '**': lambda x, y: x ** y,
