
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
    if len(operator) == 1:
        return operator[0] * operand[0] + operand[1]
    if len(operator) == 2 and operator[0] == '-':
        return operator[1] * operand[0] + operand[1]

    # This is more Pythonic way
    # return operator[0](do_algebra(operator[1:], operand)) + do_algebra(operator[1:], operand)

    # This is more Pythonic way
    # return operator[0](do_algebra(operator[1:], operand[0:1])) + do_algebra(operator[1:], operand[1:])

    # # This is Pythonic way
    # carry = 0
    # temp = []
    # for i in range(len(operator)):
    #     x = operator[i] + carry
    #     if x >= 10:
    #         carry = 1
    #         x -= 10
    #     else:
    #         carry = 0
    #     temp.insert(0, x)
    # return do_algebra(operator[1:], operand) + temp

    # # This is a bit slower way
    # result = []
    # for op in operator:
    #     temp = []
    #     for val in operand:
    #         temp.append(do_algebra([op], [val]))
    #     result.append(temp)
    # return result

    # # This is a more Pythonic way
    # return operator[0](do_algebra(operator[1:], operand[:1]),
    # do_algebra(operator[1:], operand[1:]))

    # This is the way I found it
    return operator[0](do_algebra(operator[1:], operand[:1]), do_algebra(operator[1:], operand[1:]))

