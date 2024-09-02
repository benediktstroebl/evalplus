
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
    # Your code here
    oper_list = [int(x) for x in operand]
    operator_list = operator
    results = []
    for x in oper_list:
        if x < 0:
            x = -1 * x
        results.append(x)
    if operator_list[0] == '+':
        return sum(results)
    elif operator_list[0] == '-':
        return results[0] - results[1]
    elif operator_list[0] == '*':
        return results[0] * results[1]
    elif operator_list[0] == '//':
        return results[0] // results[1]
    elif operator_list[0] == '**':
        return results[0] ** results[1]
