
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
    # operators = ['+', '-', '*', '//', '**']
    # if len(operator)!= len(operand) - 1 or not (set(operator).issubset(operators) and len(operator) >= 1) or not all([type(e) == int for e in operand]):
    #     return "Error"

    # variables
    op = operand.pop(0)
    result = op
    i = 0

    while len(operand) > 0:
        op = operator.pop(0)
        op_next = operator[0] if len(operator) > 0 else None
        op_previous = operator[-1] if len(operator) > 0 else None
        op2 = operand.pop(0)

        if op == '+':
            result += op2
        elif op == '-':
            result -= op2
        elif op == '*':
            result *= op2
        elif op == '//':
            result //= op2
        elif op == '**':
            result **= op2
        else:
            pass

        i += 1

    return result
