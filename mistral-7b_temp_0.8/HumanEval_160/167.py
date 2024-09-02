
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
    op = [None] * len(operator)
    val = [None] * len(operator)
    for i in range(len(operator)):
        op[i] = operator[i]
        val[i] = operand[i + 1]

    if len(operator) == 3:
        if op[0] == "+":
            result = val[0] + val[1]
        elif op[0] == "-":
            result = val[0] - val[1]
        elif op[0] == "*":
            result = val[0] * val[1]
        elif op[0] == "//":
            result = val[0] // val[1]
        elif op[0] == "**":
            result = val[0] ** val[1]
    elif len(operator) == 2:
        if op[0] == "+":
            result = val[0] + val[1]
        elif op[0] == "-":
            result = val[0] - val[1]
        elif op[0] == "*":
