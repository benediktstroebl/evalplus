
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
    operand_list = operand[:]
    operator_list = operator[:]
    operand_list.append(0)
    for i in range(1, len(operator_list)):
        operator_list.pop(0)
        operator_list.insert(0, operator_list.pop(0))
        operator_list.pop(0)
        for j in range(len(operand_list)):
            operand_list[j] = operator_list[j]
            if j < len(operator_list) - 1:
                operand_list[j] *= operator_list[j]
                operand_list[j] = operator_list[j] + operand_list[j]
                break
    return operand_list[0]
