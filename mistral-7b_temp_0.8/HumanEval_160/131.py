
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
    # your code here
    #first convert list to string
    op = str(operator)
    op = op.replace("'", "")
    op = op.replace("[", "")
    op = op.replace("]", "")
    op = op.replace(" ", "")
    #first convert list to string
    op2 = str(operand)
    op2 = op2.replace("'", "")
    op2 = op2.replace("[", "")
    op2 = op2.replace("]", "")
    op2 = op2.replace(" ", "")
    #fix operator and operand to be the same size
    if len(op) == len(op2):
        pass
    elif len(op) < len(op2):
        while len(op) < len(op2):
            op = op + ","
        op = op.split(",")
    elif len(op) > len(op2):
        while len(op2) < len(op):
            op2 = op2 + ","
        op2 = op2.split(",")

    #create a blank list to hold the result
