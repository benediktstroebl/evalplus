
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
        raise Exception('The length of operator list is equal to the length of operand list minus one.')
    operator_list = operator
    operand_list = operand
    operand_list[0] = 0
    for i in range(0, len(operator_list)):
        for j in range(i+1, len(operator_list)):
            if operand_list[i] and operand_list[j] > 0:
                operand_list[j] = operand_list[i] * operand_list[j]
                operand_list[i] = 0
            elif operand_list[i] and operand_list[j] < 0:
                operand_list[j] = operand_list[i] * operand_list[j]
                operand_list[i] = 0

    for i in range(0, len(operator_list)):
        if operand_list[i] == 0:
            operand_list[i] = 1
            continue
        if operand_list
