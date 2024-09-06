
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
    operand = [int(x) for x in operand]
    operator = [int(x) for x in operator]

    if len(operator) < len(operand):
        raise ValueError("Operator list should be of the same length as operand list.")

    operator_index = 0
    operand_index = 0
    operator_num = 1
    result = 0

    while operator_index < len(operator) and operand_index < len(operand):
        operator_num = operator_index + 1
        operator_type = operator[operator_num-1]
        operand_num = operand_index + 1
        operand_type = operand[operand_num-1]

        # switch the operand
        if operand_type == '+':
            operand_num += 1
            operand_type = operand[operand_num-1]
        elif operand_type == '-':
            operand_num -= 1
            operand_type = operand[operand_num-1]

        # perform the operation
        if operator_type == operand_type:
            if operator_type == '+':
                result = result + operand[operand_num-1]
            elif operator_type == '-':
                result = result - operand[operand_num-1]
            elif operator_type == '*':
                result = result * operand[operand_num-1]
            elif operator_type == '//':
                result = result // operand[operand_num-1]
            elif operator_type == '**':
                result = result ** operand[operand_num-1]
        elif operator_type == '+':
            result = result + operand[operand_num-1]
        elif operator_type == '-':
            result = result - operand[operand_num-1]
        elif operator_type == '*':
            result = result * operand[operand_num-1]
        elif operator_type == '//':
            result = result // operand[operand_num-1]
        elif operator_type
