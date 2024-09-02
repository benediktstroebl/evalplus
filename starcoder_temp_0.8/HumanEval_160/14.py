
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
    
    # base case
    if len(operator) == 0:
        return operand[0]

    # recursive case
    else:
        operand1 = operand[0]
        operator1 = operator[0]
        operand2 = operand[1]
        operator2 = operator[1:]
        operand3 = operand[2:]
        if operator1 == '+':
            return do_algebra(operator2, operand2) + operand1
        elif operator1 == '-':
            return do_algebra(operator2, operand2) - operand1
        elif operator1 == '*':
            return do_algebra(operator2, operand2) * operand1
        elif operator1 == '//':
            return do_algebra(operator2, operand2) // operand1
        else:
            return do_algebra(operator2, operand2) ** operand1
