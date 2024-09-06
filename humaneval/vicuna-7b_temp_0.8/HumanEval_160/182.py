
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
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list is not correct.")
    
    # Start with the first operand
    result = operand[0]
    
    # Use the operator list to perform the operations
    for i, op in enumerate(operator):
        if i == 0:
            # Perform the first operation
            if op == '+':
                result = result + operand[1]
            elif op == '-':
                result = result - operand[1]
            elif op == '*':
                result = result * operand[1]
            elif op == '//':
                result = result // operand[1]
            elif op == '**':
                result = result ** operand[1]
            else:
                raise ValueError("Invalid operator")
        elif i == len(operator)-1:
            # Perform the last operation
            if op == '+':
                result = result + operand[1]
            elif op == '-':
                result = result - operand[1]
            elif op == '*':
                result = result * operand[1]
            elif op == '//':
                result = result // operand[1]
            elif op == '**':
                result = result ** operand[1]
            else:
                raise ValueError("Invalid operator")
    
    return result