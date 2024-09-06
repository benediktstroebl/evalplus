
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
    from operator import add, sub, mul, floordiv, pow

    # Lookup the function for the operator and get a result from it
    operator_funcs = {
        "+": add,
        "-": sub,
        "*": mul,
        "//": floordiv,
        "**": pow
    }

    # We will be going from left to right in the operator list, 
    # so we can slice the operator and operand lists to work with
    result = operand[:-1]
    for op in operator:
        func = operator_funcs[op]
        result = [func(result[0], result[1])] + result[2:]
    return result[0]

