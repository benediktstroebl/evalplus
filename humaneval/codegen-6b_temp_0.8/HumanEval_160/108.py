
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
    if operator == []:
        return operand[0]
    else:
        operator_index = fc(operator, 0, len(operator) - 1)
        operand_index = operator_index + 1

        if operator[operator_index] == '+':
            return operand[operand_index - 1] + do_algebra(operator, operand)
        elif operator[operator_index] == '-':
            return operand[operand_index - 1] - do_algebra(operator, operand)
        elif operator[operator_index] == '*':
            return operand[operand_index - 1] * do_algebra(operator, operand)
        elif operator[operator_index] == '//':
            return operand[operand_index - 1] // do_algebra(operator, operand)
        elif operator[operator_index] == '**':
            return operand[operand_index - 1] ** do_algebra(operator, operand)
