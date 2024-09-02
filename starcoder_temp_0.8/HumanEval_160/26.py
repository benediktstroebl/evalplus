
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
    # Initialization
    result = operand[0]
    op = operator[0]
    # Using zip to go through two lists simultaneously
    for item1, item2 in zip(operator[1:], operand[1:]):
        if op == '+':
            result += item2
        elif op == '-':
            result -= item2
        elif op == '*':
            result *= item2
        elif op == '//':
            result //= item2
        elif op == '**':
            result **= item2
        else:
            raise ValueError(f"Operator {op} is not defined")
        op = item1
    return result

