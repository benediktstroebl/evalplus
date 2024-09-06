
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
    # when we want to make a return, we must be careful in the cases that
    # the loop only run once and the condition is false. 
    # Example:
    # if operator[0] == '+':
    #     return operand[0] + operand[1]
    # else:
    #     return operand[0] - operand[1]
    # this return the wrong result. 
    
    # we can use the following way instead.
    # if operator[0] == '+':
    #     total = operand[0] + operand[1]
    # else:
    #     total = operand[0] - operand[1]
    # return total
    total = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            total += operand[i+1]
        if operator[i] == '-':
            total -= operand[i+1]
        if operator[i] == '*':
            total *= operand[i+1]
        if operator[i] == '//':
            total //= operand[i+1]
        if operator[i] == '**':
            total **= operand[i+1]
    return total

