
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

    # 1st solution, with if-else
    # O(n) time | O(1) space
    '''
        result = operand[0]
        for idx in range(1, len(operand)):
            if operator[idx - 1] == '+':
                result += operand[idx]
            elif operator[idx - 1] == '-':
                result -= operand[idx]
            elif operator[idx - 1] == '*':
                result *= operand[idx]
            elif operator[idx - 1] == '//':
                result = result // operand[idx]
            else:
                result = result ** operand[idx]
        return result
    '''

    # 2nd solution, with dictionary
    # O(n) time | O(1) space
    '''
        result = operand[0]
        map_dict = {'+': operator.__add__, '-': operator.__sub__, 
                    '*': operator.__mul__, '//': operator.__floordiv__, '**': operator.__pow__}
        for idx in range(1, len(operand)):
            result = map_dict[operator[idx - 1]](result, operand[idx])
        return result
    '''

    # 3rd solution, with one-line solution
    # O(n) time | O(1) space
    return operand[0] if len(operand) == 1 else eval(''.join(map(str, operand)))
