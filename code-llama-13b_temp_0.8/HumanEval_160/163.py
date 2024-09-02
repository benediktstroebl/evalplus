
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
    while operator:
        operand_1 = operand.pop(0)
        operand_2 = operand.pop(0)
        operator_1 = operator.pop(0)
        if operator_1 == "+":
            operand.insert(0, operand_1 + operand_2)
        elif operator_1 == "-":
            operand.insert(0, operand_1 - operand_2)
        elif operator_1 == "*":
            operand.insert(0, operand_1 * operand_2)
        elif operator_1 == "//":
            operand.insert(0, operand_1 // operand_2)
        elif operator_1 == "**":
            operand.insert(0, operand_1 ** operand_2)
    return operand[0]

