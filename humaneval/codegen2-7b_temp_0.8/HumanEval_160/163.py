
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
    if len(operator)!= len(operand) - 1:
        raise ValueError(
            "The length of operator list is not equal to the length of operand list minus one."
        )
    for op in operator:
        if op not in ["+", "-", "*", "//", "**"]:
            raise ValueError(
                "Operator list is not a list of basic algebra operations."
            )
    return eval(str(operator[0]) + str(operand[0]) + " ".join(operator[1:] + [operand[-1]]))

