
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
    if len(operator) < len(operand):
        raise ValueError("The length of operator list is not equal to the length of operand list")
    if len(operator) == 0:
        raise ValueError("Operator list must have at least one operator")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands")

    if operator[0] == '*':
        operator = operator[1:]
    else:
        operator = operator[0]

    operator_evaluation = eval(operator)
    operand_evaluation = 1

    for i in range(0, len(operand), 2):
        operator_evaluation = operator_evaluation * operand[i]
        operand_evaluation *= operand[i+1]

    return operator_evaluation * operand_evaluation
