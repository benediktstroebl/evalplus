
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
    def do_addition(operator, operand):
        return operator[0] + operator[1]

    def do_subtraction(operator, operand):
        return operator[0] - operator[1]

    def do_multiplication(operator, operand):
        return operator[0] * operator[1]

    def do_floor_division(operator, operand):
        return operator[0] // operator[1]

    def do_exponentiation(operator, operand):
        return operator[0] ** operator[1]

    lookup = {'+': do_addition, '-': do_subtraction, '*': do_multiplication, '/': do_floor_division, '**': do_exponentiation}

    if operator[0] == '**':
        return do_exponentiation(operator, operand)

    if operator[0] == '/':
        result = divmod(operand[0], operand[1])
        return result[0]

    return lookup[operator[0]](operator, operand)

