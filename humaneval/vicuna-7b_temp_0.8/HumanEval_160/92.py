
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
    # Check the length of operator list
    if len(operator) != len(operand) - 1:
        return 0

    # Initialize the result to 0
    result = 0

    # Iterate through the operands
    for i in range(len(operand)):
        # Check the operator
        if i == 0:
            # Addition
            if operator[i] == '+':
                # Multiply the current value by the operator
                result = operand[i] * operand[i + 1]
                # Keep track of the current position
                i += 1
                break
            elif operator[i] == '-':
                # Multiply the current value by the operator
                result = operand[i] * operand[i + 1]
                # Keep track of the current position
                i += 1
                break
        elif operator[i] == '*':
            # Multiply the current value by the operator
            result = operand[i] * operand[i + 1]
            # Keep track of the current position
            i += 1
            break
        elif operator[i] == '/':
            # Floor division
            if i + 1 >= len(operand):
                return 0
            else:
                result = operand[i] / operand[i + 1]
                # Keep track of the current position
                i += 2
                break
        elif operator[i] == '**':
            # Exponentiation
            if i + 1 >= len(operand):
                return 0
            else:
                result = operand[i] ** operand[i + 1]
                # Keep track of the current position
                i += 2
                break
        else:
            return 0

    return result
