
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
    operand = [int(x) for x in operand]  # convert operand to integers
    operator_length = len(operator)  # check operator length
    operand_length = len(operand)  # check operand length
    operand_count = operand_length - operator_length + 1

    result = operator[0]
    for operator_index in range(operator_length):
        if not operator[operator_index]:
            raise ValueError(f"Operator '{operator_index}' is not defined")
        operand_index = operand_count - 1 - operator_index
        operand_expr = operand[operand_index]
        if operand_expr == 0:
            raise ValueError(f"Operand '{operand_index}' is zero")
        if operator_index < 0:
            result = -result
        if operator_index == 0:
            result = operand_expr
        if operator_index == 1:
            result = result * operand_expr
        if operator_index == 2:
            result = result / operand_expr
        if operator_index == 3:
            result = pow(result, operand_expr)
        if operator_index == 4:
            result = result ** operand_expr
        result = f"{result} {operator[operator_index]} {operand_expr}"
    return eval(result)