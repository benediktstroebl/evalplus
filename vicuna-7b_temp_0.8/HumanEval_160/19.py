
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
    # Check if the operator is a valid operator
    if not operator or not all(isinstance(op, str) for op in operator):
        return None

    # Check if the operand is a list of non-negative integers
    if not all(isinstance(num, int) and num >= 0 for num in operand):
        return None

    # Check if the operator is a valid operator
    if not all(isinstance(op, str) for op in operator):
        return None

    # Get the result
    try:
        # Get the number of operands
        n = len(operand)
        # Check the number of operands
        if n == len(operator):
            # Check the number of operators
            if len(operator) != len(operator.keys()):
                return None
            # Get the operator and operands
            operator = operator.keys()
            operand = operand.copy()
        # Get the operator
        operator = operator[-1]
        # Get the operands
        operand = operand[:-1]
        # Get the result
        result = eval(operator)(operand)
        return result
    except:
        return None