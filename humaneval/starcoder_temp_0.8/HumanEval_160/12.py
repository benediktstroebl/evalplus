
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

    # Create a dictionary for the operator
    d = {
        '+': operator.index('+') if '+' in operator else None,
        '-': operator.index('-') if '-' in operator else None,
        '*': operator.index('*') if '*' in operator else None,
        '//': operator.index('//') if '//' in operator else None,
        '**': operator.index('**') if '**' in operator else None
    }

    # Run through the operator list and generate the arithmetic expression
    expr = ''
    for i in range(len(operator)):
        expr += str(operand[i])
        if operator[i] == '+':
            expr += '+'
        elif operator[i] == '-':
            expr += '-'
        elif operator[i] == '*':
            expr += '*'
        elif operator[i] == '//':
            expr += '//'
        elif operator[i] == '**':
            expr += '**'

    # Evaluate the expression and return the result
    return eval(expr)
