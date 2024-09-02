
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
    # Operator precedence
    precedence = {'+':1, '-':1, '*':2, '**':3, '//':3}
    # Operator map
    ops = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '**': lambda a,b: a**b,
        '//': lambda a,b: a//b
    }
    # Evaluate expression
    i = 0
    while i < len(operand)-1:
        # Take 3 consecutive elements at a time
        op1, op2, op3 = operator[i:i+3]
        # Evaluate op1 op2 op3
        if precedence[op2] >= precedence[op1]:
            op1 = ops[op1](operand[i], operand[i+1])
            operator.pop(i)
            operand.pop(i+1)
        else:
            i += 1
        operand[i] = op1
        operator.pop(i)
    return operand[0]

