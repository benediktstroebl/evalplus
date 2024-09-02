
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
    op_index = 0
    operand_index = 0
    operator_stack = []
    result = 0

    while op_index < len(operator) - 1:
        operand_value = operand[operand_index]
        operator_value = operator[op_index]

        if operator_value in ['+', '-']:
            result = do_math(result, operator_value, operand_value)
            op_index += 1
            operand_index += 1
        elif operator_value == '*':
            operand_index += 1
            result *= operand_value
        elif operator_value == '/':
            operand_index += 1
            result //= operand_value
        elif operator_value == '**':
            operand_index += 1
            result **= operand_value
        op_index += 1
    return result
