
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

    if not (isinstance(operator, list) and isinstance(operand, list)):
        raise TypeError("operator and operand must be a list")

    if (len(operator) == 0 or len(operator)!= len(operand) - 1):
        raise ValueError("operator list length must be equal to operand list length - 1")

    if not (all(elem in ["+", "-", "*", "//", "**"] for elem in operator) and 
            all(isinstance(elem, int) for elem in operand)):
        raise TypeError("operator list must contain only + - * // ** and "
                        "operand list must contain only non-negative integers")

    expression = ""
    for i in range(len(operator)):
        expression = f"{expression}{operator[i]} {operand[i]}"
    
    return eval(expression)
