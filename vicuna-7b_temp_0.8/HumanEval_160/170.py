
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
    op = operator[0]
    ln = len(operator) - 1
    operand_len = len(operand)
    if not (op == '+' and operand[0] == '0'):
        # check if operand is a positive integer
        if (operand[0] > 0) and (operand[-1] == 0):
            operand = [int(x) for x in operand[1:-1]]
        elif (operand[0] == 0) and (operand[-1] > 0):
            operand = [int(x) for x in operand[1:-1]]
        else:
            return "Invalid operand"
    else:
        operand = [0]
    
    result = None
    for i in range(ln, len(operand)):
        operand[ln] = int(operand[ln])
        op = operator[ln]
        if op == '+':
            result = result * operand[ln] + operand[-1]
        elif op == '-':
            result = result * operand[ln] - operand[-1]
        elif op == '*':
            result = result * operand[ln] * operand[-1]
        elif op == '/':
            if operand[-1] == 0:
                return "Cannot divide by zero"
            result = result * operand[ln] // operand[-1]
        elif op == '//':
            if operand[-1] == 0:
                return "Cannot divide by zero"
            result = result * operand[ln] // operand[-1]
        elif op == '**':
            result = result * operand[ln] ** operand[-1]
    return result
