
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
    # write your code here
    from operator import add, sub, mul, truediv, pow

    # two lists of the same length
    # minus one from length of operator
    # to get the length of operand
    op = operator[:len(operator) - 1]
    op1 = operator[len(operator) - 1:]
    op2 = operand[:len(operand) - 1]
    op3 = operand[len(operand) - 1:]

    if len(operator) == 1:
        return reduce(add, operand)

    def evaluate(op1, op2, op3, func):
        return func(op1, op2) if op3 == "" else func(op1, op2, op3)

    def evaluate1(op1, op2):
        return eval(op1 + op2)

    def evaluate2(op1, op2):
        return eval(op1 + op2)

    def evaluate3(op1, op2, op3):
        return eval(op1 + op2 + op
