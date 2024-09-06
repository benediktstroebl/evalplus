
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
    def do_operation(operator, operand, operation):
        if operation == '+':
            return operator[0](operand[0]) + operator[1](operand[1])
        if operation == '-':
            return operator[0](operand[0]) - operator[1](operand[1])
        if operation == '*':
            return operator[0](operand[0]) * operator[1](operand[1])
        if operation == '//':
            return operator[0](operand[0]) // operator[1](operand[1])
        if operation == '**':
            return operator[0](operand[0]) ** operator[1](operand[1])
    
    if len(operator) != len(operand) - 1:
        return None
    
    # Using the two given lists to build the algebric expression
    new_operator = operator[:]
    while len(new_operator) > 1:
        new_operator = [do_operation(new_operator, operand, x) for x in operator]
    
    # The result of the final algebra expression 
    return new_operator[0]


