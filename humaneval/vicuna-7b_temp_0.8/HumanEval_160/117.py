
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
    # Get operator and operand
    operator = list(operator)
    operand = list(operand)

    # Remove the last operator from the operator list
    operator.pop()
    operand.pop()

    # Initialize the result and expression
    result = 0
    expression = ""

    # Check if the last operator is '**' and the operand is a number
    if operator[0] == '**' and operand[0] == int:
        # Perform exponentiation
        for i in range(len(operand) - 1):
            result = result * operand[i] ** operand[i + 1]
        result = result ** operand[-1]

    # If the last operator is not '**' or the operand is not a number, handle the operand
    else:
        # Use the last operator and the first two operands to calculate the result
        if operator[0] == '+':
            result = operand[0] + operand[1]
        elif operator[0] == '-':
            result = operand[0] - operand[1]
        elif operator[0] == '*':
            result = operand[0] * operand[1]
        elif operator[0] == '/':
            result = operand[0] / operand[1]
        elif operator[0] == '//':
            result = operand[0] // operand[1]
        else:
            # Handle the last operator according to its position
            if operator[-1] == '+':
                result = operand[0] + operand[1]
            elif operator[-1] == '-':
                result = operand[0] - operand[1]
            elif operator[-1] == '*':
                result = operand[0] * operand[1]
            elif operator[-1] == '/':
                result = operand[0] / operand[1]
            else:
                result = operand[0] ** operator[-1]

    # Return the result and expression
    return result, expression