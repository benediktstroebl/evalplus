
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
    # The algebric expression is a string of numbers
    # each operator is separated by a space
    # the first number is always the operator
    # the rest of the numbers are operands
    # note: the expression may have more than one number

    # input check
    if operator is None or len(operator) == 0:
        return None
        
    if operand is None or len(operand) == 0:
        return None

    # sort the operator and operand
    sorted_operator = sorted(operator)
    sorted_operand = sorted(list(operand))

    # calculate the expression
    expression = ""
    # loop through the sorted operator
    for i, o in enumerate(sorted_operator):
        # add the operator to the expression
        expression += str(o)
        # loop through the sorted operand
        for j, num in enumerate(sorted_operand):
            # add the operand to the expression
            # and if its the last operator, add a space
            if j == len(sorted_operand) - 1:
                expression += str(num)
            # else add the operator after the operand
            else:
                expression += str(o) + str(num)

    # eval the expression
    # note: eval() takes in a string of numbers, split by a space
    result = eval(expression)

    return str(result)

