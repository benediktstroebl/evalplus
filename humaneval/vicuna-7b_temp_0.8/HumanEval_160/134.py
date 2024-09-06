
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
    # Create empty list to store the results
    results = []
    # Keep track of the current result
    current_result = 0
    # Iterate through the operand list
    for i in range(len(operand) - 1):
        # Get the operator and operand
        operator_index = i
        operand_index = i + 1
        operator = operand[operator_index]
        operand = operand[operand_index]
        # Check if the operator is a number
        if isinstance(operator, numbers.Number):
            # If the operator is a number, use it as is
            results.append(operator)
            # Calculate the current result
            current_result = current_result * operator
        else:
            # If the operator is not a number, get the result of applying the operator to
            # the previous two results
            # Check if the operator is a plus or a minus
            if operator == '+':
                results.append(current_result)
            elif operator == '-':
                results.append(-current_result)
            # Check if the operator is a times or a divide
            elif operator == '*':
                results.append(current_result)
            elif operator == '/':
                results.append(current_result)
            # Check if the operator is an exponent
            elif operator == '**':
                results.append(current_result)
            else:
                # If the operator is not recognized, raise an error
                raise Exception("Invalid operator: " + operator)
    # Return the final result
    return current_result
