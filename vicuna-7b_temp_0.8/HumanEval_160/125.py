
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
    # Check if operator is defined
    if operator[0] == '+':
        operator = operator[1:]
        operand = operand[1:]
    elif operator[0] == '-':
        operator = operator[1:]
        operand = operand[1:]
    elif operator[0] == '*':
        operator = operator[1:]
        operand = operand[1:]
    elif operator[0] == '**':
        operator = operator[1:]
        operand = operand[1:]
    else:
        raise ValueError("Operator is not defined")

    # Check if operand is defined
    if len(operand) < 2:
        raise ValueError("Operand is empty")

    # Check if operator is defined
    if len(operator) == 0:
        raise ValueError("Operator is empty")

    # Get operand length
    n = len(operand)

    # Create empty list for result
    result = []

    # Evaluate expression
    for i in range(n):
        # Get operator and operand
        operator_index = i + 1
        operand_index = i + 1
        operator = operator[operator_index - 1]
        operand = operand[operand_index - 1]

        # Evaluate the expression
        if operator == '+':
            result.append(operand)
        elif operator == '-':
            result.append(-operand)
        elif operator == '*':
            result.append(operand)
        elif operator == '**':
            result.append(operand)
        else:
            raise ValueError("Operator is not defined")

    # Convert result to integer
    result = [int(x) for x in result]

    # Return result
    return sum(result)
