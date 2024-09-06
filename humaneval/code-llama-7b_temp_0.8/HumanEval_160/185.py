
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
    # Your code here
    operand = operand
    operator = operator
    oprand_len = len(operand)
    oprand_itr = 0
    for operator_itr in range(oprand_len - 1):
        oprand_itr += 1
        operand_value = operand[oprand_itr]
        operator_value = operator[operator_itr]
        operand[oprand_itr] = eval(str(operand[oprand_itr - 1]) + operator_value + str(operand_value))
    return eval(str(operand[oprand_itr]))


