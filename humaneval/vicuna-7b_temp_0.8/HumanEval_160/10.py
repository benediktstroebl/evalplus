
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
    # Check if the operator list is empty
    if len(operator) == 0:
        raise ValueError("Operator list must not be empty")

    # Check if the operand list is empty
    if len(operand) == 0:
        raise ValueError("Operand list must not be empty")

    # Check if the operator list has at least one operator
    if len(operator) == 0:
        raise ValueError("Operator list must have at least one operator")

    # Check if operand list has at least two operands
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands")

    # Get the first operand from the operand list
    left = operand[0]

    # Get the operator from the operator list
    operator = operator[0]

    # Get the next operator from the operator list
    right = operator[1]

    # Get the operand from the operand list
    right = operand[1]

    # Check if the operator is the last operator in the operator list
    if right != "":
        raise ValueError("The last operator in the operator list must be a multiplication operator")

    # Check if the operand is a number
    if not isinstance(left, int) and not isinstance(right, int):
        raise ValueError("Operand must be a number")

    # Check if the operand is negative
    if isinstance(right, int):
        if right < 0:
            raise ValueError("Operand must not be negative")

    # Evaluate the expression
    if operator == "+":
        result = left + int(right)
    elif operator == "-":
        result = left - int(right)
    elif operator == "*":
        result = left * int(right)
    elif operator == "/":
        result = int(left) / int(right)
    elif operator == "**":
        result = pow(int(left), int(right))
    else:
        raise ValueError("Invalid operator")

    # Return the result
    return result