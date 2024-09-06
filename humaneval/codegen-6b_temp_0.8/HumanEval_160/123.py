
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
    
    # process the operand, in case it's not a list of integers
    if not isinstance(operand, list):
        operand = [operand]

    # process the operator
    # condition: operand has at least two elements
    # assume user click on a button with no operator, so '+' is default operator
    if len(operand) < 2:
        return operand[0]

    # loop through the list, skip the last element as operator
    operator_length = len(operator) - 1
    for i in range(operator_length):
        # if operator is '*' or '/', find the operator_id and operand_id
        # assume user click on a button with multiple operator, so '*' is default operand
        if operator[i] == '*':
            operator_id = i
            operand_id = operator_id + 1
        elif operator[i] == '/':
            operator_id = i
            operand_id = operator_id + 1

        # get the operator
        operator_value = operator[operator_id]
        # get the operand
        operand_value = operand[operand_id]

        # calculate the result
        if "*" == operator_value:
            operand[operand_id] = operand_value * operand[operand_id + 1]
            # remove the last value
            operand.pop()
        elif "-" == operator_value:
            # assume user click on a button with only -, so result is -
            operand[operand_id] = - operand[operand_id + 1]
            # remove the last value
            operand.pop()
        elif "+" == operator_value:
            # assume user click on a button with only +, so result is +
            operand[operand_id] = operand[operand_id + 1]
            # remove the last value
            operand.pop()
        elif "/" == operator_value:
            # condition: operand_value >= 0
            operand[operand_id] = operand[operand_id + 1] // operand[operand_id]