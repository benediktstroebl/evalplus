
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
    # Check if operator list is not empty and operand list is not empty
    if len(operator) > 0 and len(operand) > 1:
        # Get the first operator from operator list
        operator = operator.pop(0)

        # Get the first operand from operand list
        operand = operand[0]

        # Create a empty list to store the result
        result = []

        # Loop through each operand in operand list
        for operand in operand:
            # Evaluate the expression
            expression = []
            for operator in operator:
                # Check if the operator is a valid operator for the current operand
                if operator[0] == operator[1] == '*':
                    # Multiply the current operator with the current operand
                    expression.append(operand * operand)
                elif operator[0] == operator[1] == '/':
                    # Divide the current operator with the current operand
                    expression.append(operand / operand)
                elif operator[0] == operator[1] == '**':
                    # Raise the current operator to the power of the current operand
                    expression.append(pow(operand, operand))
                else:
                    # Add the current operator with the current operand
                    expression.append(operator + operand)

            # Add the expression to the result
            result.append(expression)

        # Concatenate all the sub-expressions in result
        result = ''.join(result)

        # Remove all leading and trailing zeroes from the result
        result = remove_leading_zeroes(result)
        result = remove_trailing_zeroes(result)

        # Check if the result is not empty and return the value of the expression
        if len(result) > 0:
            return eval(result)
    return 'Invalid Operand'
