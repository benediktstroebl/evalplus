
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
    # 将数组转化为数字进行运算
    operand = [int(n) for n in operand]
    # 将操作符进行转化
    operator = [i for i in operator]
    operator_num = len(operator)
    # 根据操作符长度，构建操作数数组
    operand_num = []
    operand_num.append(0)
    for i in range(operator_num):
        operand_num.append(operand_num[i] + 1)
    # 逐个操作符，将操作数进行操作
    for i in range(operator_num):
        op = operator.pop(0)
        if op == '+':
            operand[operand_num[i]] = operand[operand_num[i]] + operand[operand_num[i] + 1]
        elif op == '-':
            operand[operand_num[i]] = operand[operand_num[i]] - operand[operand_num[i] + 1]
        elif op == '*':
            operand[operand_num[i]] = operand[operand_num[i]] * operand[operand_num[i] + 1]
        elif op == '//':
            operand[operand_num[i]] = operand[operand_num[i]] // operand[operand_num[i] + 1]
        elif op == '**':
            operand[operand_num[i]] = operand[operand_num[i]] ** operand[operand_num[i] + 1]
        operand.pop(operand_num[i] + 1)
        for j in range(i, operator_num):
            operand_num[j] = operand_num[j] - 1
    return operand[0]
