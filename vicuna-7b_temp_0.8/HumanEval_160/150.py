
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
        raise ValueError('Operator list and operand list have different length')

    # Get the first operand
    first_operand = operand[0]
    operand = operand[1:]

    # Get the operator and operand
    operator_index = 0
    operator_value = operator[operator_index]
    operator_is_mult = len(operator_value) == 2
    operator_index += 1

    for i in range(len(operand)):
        result = eval_single_operand(first_operand, operand[i], operator_value, operator_is_mult)
        first_operand = result

    return eval_single_operand(first_operand, operand[-1], operator_value, operator_is_mult)
