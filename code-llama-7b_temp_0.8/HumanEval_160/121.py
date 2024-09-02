
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
    # 初始化
    result = 0
    # 操作数
    operand_left = operand[:-1]
    # 操作符
    operator_list = operator[:-1]
    # 先计算中间值
    for i in range(len(operator_list)):
        if operator_list[i] == '+':
            result += operand_left[i]
        elif operator_list[i] == '-':
            result -= operand_left[i]
        elif operator_list[i] == '*':
            result *= operand_left[i]
        elif operator_list[i] == '//':
            result //= operand_left[i]
        elif operator_list[i] == '**':
            result **= operand_left[i]
    # 计算最后一个值
    result += operand[-1]
    return result
