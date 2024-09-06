
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
    if len(operator) < 1 or len(operand) < 2:
        return 0
    for i in range(len(operator)):
        if operator[i] == '*':
            op = operand[i]
            if i == len(operator) - 1:
                operator = operator[:-1]
            if i == 0:
                operator = operator[1:]
            result = do_algebra(operator, [op] + [x for x in operand[i+1:] if x != 0])
            for j in range(len(result)-1, len(result)):
                result = result[:j] * result[j+1]
    return 0
