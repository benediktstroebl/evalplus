
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
    # my solution
    # from operator import add, mul, sub, floordiv, pow
    # op_dic = {
    #     '+':add,
    #     '-':sub,
    #     '*':mul,
    #     '//':floordiv,
    #     '**':pow
    # }
    # op = [op_dic[i] for i in operator]
    # return eval(
    #     functools.reduce(lambda x, y: str(x)+i+str(y), [str(i) for i in operand])
    # )

    # Tortoise solution
    # from functools import reduce
    # from operator import add, mul, sub, floordiv, pow

    # op_dic = {
    #     '+': add,
    #     '-': sub,
    #     '*': mul,
    #     '//': floordiv,
    #     '**': pow
    # }
    # op = [op_dic[i] for i in operator]
    # return eval(
    #     functools.reduce(lambda x, y: str(x) + i + str(y), [str(i) for i in operand])
    # )

    # horror solution
    # from functools import reduce
    # from operator import add, mul, sub, floordiv, pow
    # op_dic = {
    #     '+': add,
    #     '-': sub,
    #     '*': mul,
    #     '//': floordiv,
    #     '**': pow
    # }
    # op = [op_dic[i] for i in operator]
    # return reduce(lambda x, y: op[x](x, y), [int(i) for i in operand])
