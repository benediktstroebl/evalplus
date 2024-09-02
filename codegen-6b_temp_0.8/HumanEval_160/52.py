
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
    # Write your code here.
    
    # Make sure operator is a list, and operand is a list of integers.
    if not isinstance(operator, list):
        raise Exception('Parameter "operator" must be a list.')
    if not isinstance(operand, list) or not all([isinstance(x, int) for x in operand]):
        raise Exception('Parameter "operand" must be a list of integers.')
    if len(operator) != len(operand) - 1:
        raise Exception('Operand and operator must have the same length')
    
    # Set up the algebric expression to reduce to one number.
    number = operand[-1]
    for i in range(len(operand)-2, -1, -1):
        number = operator[i] + number
        
    return number
