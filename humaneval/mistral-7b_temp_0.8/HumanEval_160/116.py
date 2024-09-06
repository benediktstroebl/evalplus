
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
    assert len(operator) == len(operand)-1, "Incorrect length of lists"
    assert all(x in ['+','-','*','//','**'] for x in operator), "Incorrect list of operators"
    assert all(x >= 0 for x in operand), "Incorrect list of operands"
    if len(operand) == 1:
        return operand[0]
    res = operand[0]
    for i,o in enumerate(operator):
        if i == 0:
            res += operand[i+1]
        if o == '+':
            res += operand[i+1]
        if o == '-':
            res -= operand[i+1]
        if o == '*':
            res *= operand[i+1]
        if o == '//':
            res //= operand[i+1]
        if o == '**':
            res = res ** operand[i+1]
    return res
