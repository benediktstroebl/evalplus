
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
    # Checking the length of operator and operand.
    if len(operator) != len(operand) - 1:
        return None

    # If the expression contains a division operator, check for division by 0.
    if '//' in operator:
        if any(val == 0 for val in operand):
            return None

    # Creating a stack to evaluate the expression.
    stack = []

    # Iterating through the list of operands and operators.
    for i in range(len(operator)):
        if operator[i] == '+':
            stack.append(sum(stack))
        elif operator[i] == '-':
            stack.append(stack.pop() - operand[i])
        elif operator[i] == '*':
            stack.append(stack.pop() * operand[i])
        elif operator[i] == '//':
            stack.append(stack.pop() // operand[i])
        elif operator[i] == '**':
            stack.append(stack.pop() ** operand[i])

    return stack[-1]
