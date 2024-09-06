
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

    # iterate over operator list
    for i in range(len(operator)):
        # find first and second element in the operand list
        first = operand[i]
        second = operand[i+1]
        # get the operator that connects the two elements
        op = operator[i]
        # execute the operation based on the operator
        if op == "+":
            first = first + second
        elif op == "-":
            first = first - second
        elif op == "*":
            first = first * second
        elif op == "//":
            first = first // second
        elif op == "**":
            first = first ** second
        
        # create a new list with the updated operand element
        operand.pop(i+1)
        operand.insert(i+1, first)
    
    # return the last element of the operand list
    return operand[len(operand) - 1]

