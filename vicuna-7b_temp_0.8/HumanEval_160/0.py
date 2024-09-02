
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
    if len(operator) < 1:
        raise ValueError("Operator list should have at least one operator")
    if len(operator) != len(operand):
        raise ValueError("Operator list and operand list should have the same length")
    if not operator[0] in ['-', '*', '/']:
        raise ValueError("Only /, \*, - are allowed as operator")
    if not operand[0] in ['-', '*']:
        raise ValueError("Only / and \* are allowed as operand")
    
    #get the operator and operand
    operator_ = operator.pop(0)
    operand_ = operand.pop(0)
    
    #get the evaluation of the expression
    eval = 0
    if operator_ == '/':
        eval = eval // operand_
    elif operator_ == '*':
        eval = eval * operand_
    else:
        eval = eval / operand_
    
    return eval
