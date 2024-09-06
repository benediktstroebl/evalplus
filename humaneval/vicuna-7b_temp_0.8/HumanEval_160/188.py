
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
    # Get the length of operator list
    n = len(operator)
    # Get the length of operand list
    m = len(operand)
    # Check if operator list is not empty
    if n > 0:
        # Check if operand list is not empty
        if m > 1:
            # Initialize the result as an empty list
            result = []
            # Create the expression
            expression = ""
            # Iterate over the operator list
            for i in range(n):
                # Get the operator and operands
                operator_ = operator[i]
                operands = operator[i+1:i+m]
                # Get the result of the expression
                result_ = eval_expression(expression, operands)
                # Update the expression
                expression = expression + str(operator_)+"("
                expression += str(result_) + ")"
            # Update the result
            result = eval_expression(expression, operand)
    return result