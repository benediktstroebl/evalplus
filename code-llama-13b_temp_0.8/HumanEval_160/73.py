
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

    # Iterate over the operator list and perform the indicated operation.
    for index, op in enumerate(operator):

        # Addition ( + )
        if op == '+':
            operand[index] = operand[index] + operand[index+1]

        # Subtraction ( - ) 
        if op == '-':
            operand[index] = operand[index] - operand[index+1]

        # Multiplication ( * )
        if op == '*':
            operand[index] = operand[index] * operand[index+1]

        # Floor division ( // )
        if op == '//':
            operand[index] = operand[index] // operand[index+1]

        # Exponentiation ( ** )
        if op == '**':
            operand[index] = operand[index] ** operand[index+1]

        # Remove the operand that has been used.
        operand.pop(index+1)

    return operand[0]
