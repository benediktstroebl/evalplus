
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
    expression = []
    index = 0

    while index < len(operator):
        # if this is a basic algebra operator
        if operator[index] in ['+', '-', '*', '//', '**']:
            # add the operator to the expression
            expression.append(operator[index])
            # do the math
            expression.append(eval(operator[index] + '(' + str(operand[index]) + ',' + str(operand[index + 1]) + ')'))
            # remove the operator from the operator list
            del operator[index]
            # remove the two operands from the operator list
            del operator[index]
            index = 0
        # if this is a punctuation character
        else:
            # add to the expression
            expression.append(operator[index])
            index += 1
    
    return expression[0]
