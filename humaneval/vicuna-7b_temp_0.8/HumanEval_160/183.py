
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
    if not (operator[0] in ['+', '*', '-', '/', '//']):
        raise ValueError("Invalid operator")
    
    # Check if the operator is supported
    if operator[0] == '/':
        if not operator[1:]:
            raise ValueError("Invalid operator")
        return float(operand[0] / operand[1])
    else:
        if not operator:
            raise ValueError("Invalid operator")
        else:
            return operator[0](operand[0], operand[1])
