
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
    operand = [int(op[0]) for op in operand]
    operand = sorted(operand)

    # Get the operator
    operator_index = operator.index(operator[0])

    # Determine the operator and operand
    operator = operator[1:]
    operand_index = operand.index(operand[0])
    operand = operand[1:]

    if operator_index == 0:
        # Addition
        if operator_index == 0 and operand_index == 0:
            return 1
        else:
            return operator[0] + operand[0]
    elif operator_index == 1:
        # Multiplication
        if operator_index == 0 and operand_index == 0:
            return 1
        else:
            return operator[0] * operand[0]
    elif operator_index == 2:
        # Floor division
        if operand_index == 0:
            return operator[0] / operand[0]
        else:
            return operator[0] // operand[0]
    elif operator_index == 3:
        # Exponentiation
        return operator[0] ** operand[0]
    else:
        # Negative
        if operator[0] == '-':
            return -operand[0]
        else:
            return operator[0] * operand[0]
