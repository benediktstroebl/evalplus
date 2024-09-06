
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
    op_list = ['+', '-', '*', '//', '**']
    op = operator[0]
    val1 = operand[0]
    val2 = operand[1]
    for i in range(1, len(operator)):
        if op == '+':
            val1 += val2
        elif op == '-':
            val1 -= val2
        elif op == '*':
            val1 *= val2
        elif op == '//':
            val1 //= val2
        elif op == '**':
            val1 **= val2
        op = operator[i]
        val2 = operand[i+1]
    return val1

