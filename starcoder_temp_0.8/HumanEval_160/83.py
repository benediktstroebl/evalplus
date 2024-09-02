
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

    assert isinstance(operator, list), "operator must be a list"
    assert isinstance(operand, list), "operand must be a list"
    assert len(operator) == len(operand) - 1, "length of operator is not equal to length of operand - 1"
    assert set(operator).issubset(set(['+', '-', '*', '//', '**'])), "operator has an invalid operator"
    assert all(isinstance(num, int) for num in operand), "operand has an invalid number"
    assert all(num >= 0 for num in operand), "operand has a negative number"

    if len(operator) == 0:
        return operand[0]

    for i in range(len(operator)):
        if operator[i] == '+':
            operand[i + 1] += operand[i]
            operand.pop(i)
        elif operator[i] == '-':
            operand[i + 1] -= operand[i]
            operand.pop(i)
        elif operator[i] == '*':
            operand[i + 1] *= operand[i]
            operand.pop(i)
        elif operator[i] == '//':
            operand[i + 1] = operand[i + 1] // operand[i]
            operand.pop(i)
        elif operator[i] == '**':
            operand[i + 1] = operand[i + 1] ** operand[i]
            operand.pop(i)
    return operand[0]

