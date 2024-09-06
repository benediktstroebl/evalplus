
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

    # TODO: Write a solution
    # First, you need to check that the length of operator is equal to the length of operand list minus 1.
    # This is a bit tricky because you cannot simply compare the length of the two lists. You need to 
    # convert the operator list into a string and compare it with the operand list converted into a 
    # string.
    # Second, you need to check that the first element of the operator list is '+', '*', '-', or '//'.
    # Third, you need to check that all elements of the operand list are non-negative integers.
    # Last, you need to iterate over the lists and build the algebraic expression and evaluate it.

    if len(operator) != len(operand) - 1:
        return None

    operator_str = ''.join(operator)
    operand_str = ''.join(operand)

    if operator_str[0] != '+' and operator_str[0] != '*' and operator_str[0] != '-' and operator_str[0] != '//':
