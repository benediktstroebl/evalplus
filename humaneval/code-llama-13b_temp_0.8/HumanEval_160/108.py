
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
    # Make sure the operand and operator are the right length
    if len(operator) + 1 != len(operand):
        return "Wrong length for the lists"

    # Set the first number
    result = operand.pop(0)

    # Operate on the remaining operands
    while operand:
        # Get the operator
        op = operator.pop(0)

        # Get the operand
        opnd = operand.pop(0)

        # Perform the operation
        if op == '+':
            result += opnd
        elif op == '-':
            result -= opnd
        elif op == '*':
            result *= opnd
        elif op == '//':
            result //= opnd
        elif op == '**':
            result **= opnd
        else:
            return "Bad operator"
    
    # Return the result
    return result

