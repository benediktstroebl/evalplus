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
    # Algorithm
    # 1. Use the operand list to iterate through the expression list and build the expression
    # 2. Return the evaluation of the last expression in the expression list
    # var_1 = operand[0]
    # var_2 = operand[1]
    # ...
    # var_n = operand[n]
    # expression = var_1 + var_2 * var_3 - var_4 // var_5 ** var_6
    # ...
    # expression = var_1 + var_2 * expression - var_3 // var_4 ** var_5
    # ...
    # expression = expression + var_5 * var_6 - var_7 // var_8 ** var_9
    expression = operand[0]
    for i in range(1, len(operand)):
        expression = expression + operator[i-1] * operand[i]
    # 3. Return the evaluation of the expression
    return expression