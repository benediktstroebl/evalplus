
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
    # Check that operator list has at least one operator
    if len(operator) == 0:
        return None

    # Check that operand list has at least two operands
    if len(operand) == 0:
        return None

    # Check that the length of operator list is equal to the length of operand list minus one
    if len(operator) != len(operand) - 1:
        return None

    # Initialize the result list
    result = []

    # Iterate through operator list and operand list
    for operator_index, operator in enumerate(operator):
        for operand_index, operand in enumerate(operand):
            # Get the value of the operator and operand
            value = operator[operator_index]
            operand_value = operand[operand_index]

            # Get the value of the result
            if operator_index == 0:
                # Addition
                result.append(value)
            elif operator_index == 1:
                # Subtraction
                result.append(value * operand_value)
            elif operator_index == 2:
                # Multiplication
                result.append(value * operand_value)
            elif operator_index == 3:
                # Floor division
                result.append(value / operand_value)
            elif operator_index == 4:
                # Exponentiation
                result.append(value ** operand_value)
            else:
                return None

    return result