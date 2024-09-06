
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
    # Get the operator and operand from the lists
    operator = operator.tolist()
    operand = operand.tolist()
    n = len(operand)

    # Create a stack to store intermediate results
    stack = [operand[n-1]]

    # Keep pushing operands to the stack until the operator is found
    while len(stack) > 0:
        top = stack.pop()
        if operator[0] == '=':
            # If the operator is the assignment operator (=),
            # push the operand to the stack
            stack.append(top)
        else:
            # If the operator is not the assignment operator (=),
            # push the operator and the top of the stack to the result
            result.append(top)
            result.append(operator[0])
            # Apply the operator to the top of the stack and push the result to the result
            result.append(apply_operator(operator[1:], top))

    return result[::-1]
