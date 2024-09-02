
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
    # Check if operator list is not empty
    if len(operator) == 0:
        return operand

    # Check if operand is not empty
    if len(operand) == 0:
        return [0]

    # Check if operator list is not empty
    if len(operator) == 0:
        return [0]

    # Check if operand list is not empty
    if len(operand) == 0:
        return [0]

    # Check if the operator is not '**'
    if operator[0] != '**':
        # Check if the operand is not empty
        if len(operand) == 0:
            return [0]
        # Create the algebric expression
        expression = operand[0]
        # Add operator to the expression
        expression = expression + operator[1]
        for i in range(2, len(operator)):
            # Get the operator
            operator_index = operator[i]
            # Get the operands
            left = operator_index[0]
            right = operator_index[1]
            # Get the operands
            left_index = operand.index(left)
            right_index = operand.index(right)
            # Get the index of the next operator
            next_index = operand.index(operator[i+1]) if i+1 < len(operator) else -1
            # Check if the operator is '//'
            if operator[i] == '/':
                # If the right operand is 0, return 0
                if operand[right_index] == 0:
                    return [0]
                # Check if the next operator is '/'
                next_index = operand.index(operator[i+1]) if i+1 < len(operator) else -1
                # If the next operator is '/', raise an error
                if next_index == -1:
                    raise ValueError('// by zero')
                # Create the expression
                expression = expression + operand[right_index]
                # Add the operator
                expression = expression + operator[i+1]
            # If the operator is not '//', calculate the expression
