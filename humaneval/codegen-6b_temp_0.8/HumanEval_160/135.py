
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
    if not operator:
        raise Exception("Operator is empty.")
    if not operand:
        raise Exception("Operand is empty.")
    if len(operator) != len(operand) - 1:
        raise Exception("Operand is not the same length as operator.")
    if len(operator) != len(operand):
        raise Exception("Operand is not the same length as operator.")

    stack_operand = []
    for item in operand:
        stack_operand.append(item)

    result = stack_operand.pop()
    while stack_operand:
        item = stack_operand.pop()
        if item == operator[0]:
            operator_idx = 0
            result += operator[operator_idx] * item
        else:
            result -= operator[operator_idx] * item
        operator_idx = operator_idx + 1
        if operator_idx >= len(operator):
            operator_idx = 0

    return result

