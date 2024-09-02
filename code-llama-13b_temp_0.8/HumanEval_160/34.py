
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

    # Stack is used to store operand
    stack = []

    # Iterating over the operand array
    for i in range(len(operand)):
        # Push the operand on to the stack
        stack.append(operand[i])
        # If the stack size is less than 2, continue
        if len(stack) < 2:
            continue
        # Check if there is an operator
        if operator[i] in operators:
            # Pop the top two values
            num1 = stack.pop()
            num2 = stack.pop()
            # Compute the result
            result = operators[operator[i]](num1, num2)
            # Push the result back to the stack
            stack.append(result)

    # Return the last element of the stack
    return stack.pop()


    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
    '//': lambda x, y: x // y,

