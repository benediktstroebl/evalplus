
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
    lst = []
    for i in range(len(operand)-1):
        lst.append(operand[i])
    lst.append(operand[len(operand)-1])
    x = lst[0]
    for i in range(1,len(lst)):
        if i%2 == 0:
            x = eval(str(x) + operator[i/2-1] + str(lst[i]))
        else:
            x = eval(str(x) + operator[(i-1)/2] + str(lst[i]))
    return x
