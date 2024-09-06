
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
    if len(operator) > 0:
        # Get the first operator
        operator_name = operator.pop(0)
        # Get the operand
        operand = operand[1:-1]
        # Get the value of the operator
        operator_value = get_operator_value(operator_name)
        # Evaluate the expression
        expression = [operator_value]
        for index in range(len(operand)):
            # Get the next operand
            operand = operand[index]
            # Get the operator
            operator = operator[1:]
            # Get the next operator
            operator = operator[0]
            # Evaluate the expression
            expression.append(get_operator_value(operator, operand))
            # Evaluate the expression
            expression.append(evaluate_expression(expression))
            # Get the value of the operator
            operator_value = get_operator_value(operator, operand)
            # Evaluate the expression
            expression.append(operator_value)
        # Return the result
        return expression[0]
    else:
        return None
