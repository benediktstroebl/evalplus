
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
    # base case
    if len(operator) == 0:
        return operand[0]
    # recursive case
    else:
        index = len(operator) - 1
        # get operator
        op = operator[index]
        # get operand
        op1 = operand[index]
        op2 = operand[index + 1]

        if op == "+":
            result = op1 + op2
        elif op == "-":
            result = op1 - op2
        elif op == "*":
            result = op1 * op2
        elif op == "//":
            result = op1 // op2
        elif op == "**":
            result = op1 ** op2
        return do_algebra(operator[:index], operand[:index]) + result



