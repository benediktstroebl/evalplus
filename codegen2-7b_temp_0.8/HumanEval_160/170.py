
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
    operator_list = operator
    operand_list = operand

    if not (operator_list and operand_list):
        return "Operator and operand list cannot be empty"
    elif len(operator_list)!= len(operand_list) - 1:
        return "Length of operator list and operand list is not equal to 1"

    operand_evaluation = 0
    for i in range(len(operator_list)):
        operand_evaluation += operator_list[i] * operand_list[i]

    return operand_
