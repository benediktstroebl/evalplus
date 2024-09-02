
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
    # Check if the length of operator list is equal to the length of operand list minus one
    if len(operator) != len(operand)-1:
        raise ValueError("The length of operator list is not equal to the length of operand list minus one")

    # Check if the operator is a valid operator and operand is not empty
    if operator[0] not in ['/', '**']:
        if not operator[1:]:
            raise ValueError("The operator is not a valid operator")
        elif not operand:
            raise ValueError("Operand is empty")
    
    # Evaluate the expression
    try:
        eval = eval_expression(operator[1:], operand)
        return eval
    except Exception as e:
        raise ValueError("The expression is not valid: {}".format(str(e)))
    
