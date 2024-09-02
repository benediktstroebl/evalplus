
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

    # YOUR CODE HERE
    # Please use the following variables
    # operator: a list with the operators
    # operand: a list with the operands
    # result: a variable to store the result
    # i: variable to use in a loop over the list

    # use a loop to go through the list
    #operator = ['+', '*', '-', '/', '**']
    #operand = [5, 3, 8, 2, 9]
    #result = 5 + 3 * 8 - 2 / 9
    #result = 5 + (3 * 8) - (2 / 9)
    #result = 5 + 24 - (2 / 9)
    #result = 29 - (2 / 9)
    #result = 29 - (2 / 9)
    #result = 29 - 0.2222222222222222

    #return result

    # for i in range(len(operator)):
    #     print(operand[i], operator[i], operand[i+1])
    #     if operator[i] == '+':
    #         operand[i] += operand[i+1]
    #     elif operator[i] == '-':
    #         operand[i] -= operand[i+1]
    #     elif operator[i] == '*':
    #         operand[i] *= operand[i+1]
    #     elif operator[i] == '/':
    #         operand[i] //= operand[i+1]
    #     elif operator[i] == '**':
    #         operand[i] **= operand[i+1]
    #     i += 1
    # return operand[0]

    # loop through list
    result = operand[0]
    i = 0
    while i < len(operator):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
        i += 1
    return result
