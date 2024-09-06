
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
    # def helper(op, res):
    #     if len(op) > 1:
    #         op0 = op.pop(0)
    #         res0 = res.pop(0)
    #         op1 = op.pop(0)
    #         res1 = res.pop(0)
    #         return helper(op, [op0(res0, res1)])
    #     else:
    #         op0 = op.pop(0)
    #         res0 = res.pop(0)
    #         return op0(res0, res.pop(0))

    # return helper(operator[:], operand[:])

    res = operand.pop(0)
    for op, val in zip(operator, operand):
        if op == '+':
            res += val
        elif op == '-':
            res -= val
        elif op == '*':
            res *= val
        elif op == '//':
            res //= val
        elif op == '**':
            res **= val

    return res

