
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
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("operator and operand length should be at least 1 and at least 2")

    operator_stack = operator
    operand_stack = operand

    operator_dict = {
        '+': operator_stack.pop(),
        '*': operator_stack.pop(),
        '-': operator_stack.pop()
    }

    operand_stack.reverse()
    result = operand_stack.pop()

    for operator in operator_stack:
        result = operate(operator_dict[operator], result, operand_stack.pop())

    return
