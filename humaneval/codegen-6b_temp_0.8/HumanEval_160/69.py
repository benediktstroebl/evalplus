
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
    #return None

    # make the operator list a list of list
    operator = [operator[i:i + len(operand)] for i in range(0, len(operator), len(operand))]
    # make the operator list a list of list of integers
    operator = [[int(operator[i][j]) for j in range(len(operator[i]))] for i in range(len(operator))]

    # turn the operand list into a list of lists of integers
    operand = [operand[i:i + len(operator)] for i in range(0, len(operand), len(operator))]
    operand = [[int(operand[i][j]) for j in range(len(operand[i]))] for i in range(len(operand))]

    # for a given operator, perform the corresponding operation on the operand list
    for i in range(len(operator)):
        result = operate(operator[i], operand[i])
        operand[i] = result

    # turn the resulting operand list into a list of integers
    operand = [int(operand[i][j]) for i in range(len(operand)) for j in range(len(operand[i]))]
    
    return operand[0]

