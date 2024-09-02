
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
    # Check if the length of operator is equal to the length of operand -1
    if len(operator) != len(operand)-1:
        return None
    
    # Check if operator has at least one operator
    if len(operator) == 0:
        return None
    
    # Check if operand is a list of non-negative integers
    if not isinstance(operand, list) or not all(map(int, operand)) or not all(map(lambda x: 0 <= x, operand)):
        return None
    
    # Initialize variables for solving equation
    result = 0
    for i, op in enumerate(operator):
        # Perform the operation and update result
        result = result * operand[i]
    
    # Evaluate result
    return result