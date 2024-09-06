
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
    operators = {
        '+': operator.index('+'),
        '-': operator.index('-'),
        '*': operator.index('*'),
        '//': operator.index('//'),
        '**': operator.index('**')
    }
    op_dict = {}
    for i in range(len(operator)):
        if operator[i] in op_dict:
            op_dict[operator[i]].append(i)
        else:
            op_dict[operator[i]] = [i]
    for k, v in op_dict.items():
        if len(v) == 1:
            pass
        else:
            index_0 = v[0]
            index_1 = v[1]
            if index_0 > 0:
                index_0 -= 1
            if index_1 < len(operator) - 1:
                index_1 += 1
            operator = operator[:index_0] + operator[index_1:]
            operator[index_0] = k
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]
        else:
            pass
    return result

