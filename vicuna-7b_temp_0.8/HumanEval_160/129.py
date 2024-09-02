
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
    # the number of operands
    num_ops = len(operand)
    # the list of all the operators in operator list
    operator_list = [operator.pop(0)]
    # the list of all the operands in operator list
    operand_list = [operand.pop(0)]

    # push the operators and operands into the operator and operand list
    while len(operator_list) > 0:
        operator = operator_list.pop(0)
        operand = operand_list.pop(0)
        if operator == '**':
            result = _exponentiation(operator_list, operand_list, operand)
        elif operator == '//':
            result = _floordiv(operator_list, operand_list, operand)
        elif operator in ['+', '-', '*', '']:
            result = _arithmetic(operator_list, operand_list, operand)
        operator_list.append(operator)
        operand_list.append(operand)

    return result
