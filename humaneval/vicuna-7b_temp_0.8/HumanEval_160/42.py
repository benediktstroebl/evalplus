
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
    # The length of operator list is equal to the length of operand list minus one.
    if len(operator) < len(operand) - 1:
        return None
    elif len(operator) == len(operand) - 1:
        operand = [int(op) for op in operand] # convert operand to integers
        result = 0
        for i in range(0, len(operand), 2):
            op1 = operator[0]
            op2 = operator[1]
            if op1 == '+':
                result += operand[i] * operand[i + 1]
            elif op1 == '-':
                result += operand[i] * operand[i + 1] * -1
            elif op1 == '*':
                result += operand[i] * operand[i + 1]
            elif op1 == '/':
                result += operand[i] * operand[i + 1]
            elif op1 == '**':
                result *= operand[i]
            operator.pop(0)
            operand.pop(0)
        return result
    else:
        return None