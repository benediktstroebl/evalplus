
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
    if len(operator)!= len(operand)-1:
        raise Exception('Operator and Operand length does not match.')

    results = []
    for i, o in enumerate(operator):
        if o == '+':
            results.append(operand[i] + operand[i+1])
        elif o == '-':
            results.append(operand[i] - operand[i+1])
        elif o == '*':
            results.append(operand[i] * operand[i+1])
        elif o == '//':
            results.append(int(operand[i] // operand[i+1]))
        elif o == '**':
            results.append(operand[i] ** operand[i+1])

    return sum(
