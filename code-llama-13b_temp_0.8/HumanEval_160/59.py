
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

    if len(operator) == 0 or len(operand) < 2:
        return None

    # if operand contains only 1 number, the result is just that number.
    if len(operand) == 1:
        return operand[0]

    # if operand contains only 2 numbers, return the result of calculation.
    if len(operand) == 2:
        if operator[0] == '+':
            return operand[0] + operand[1]
        elif operator[0] == '-':
            return operand[0] - operand[1]
        elif operator[0] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '//':
            return operand[0] // operand[1]
        elif operator[0] == '**':
            return operand[0] ** operand[1]
        else:
            return None

    # if operand contains more than 2 numbers, return the result of calculation.
    if len(operator) == len(operand) - 1:
        # initialize variables
        i = 0
        j = 1
        k = 0
        result = 0
        # calculate result
        while i < len(operand) - 1:
            if operator[i] == '+':
                result += operand[j]
            elif operator[i] == '-':
                result -= operand[j]
            elif operator[i] == '*':
                result *= operand[j]
            elif operator[i] == '//':
                result //= operand[j]
            elif operator[i] == '**':
                result **= operand[j]
            else:
                return None
            i += 1
            j += 1
        return result

    # if length of operator is more than length of operand, return None.
    if len(operator) > len(operand) - 1:
        return None

    # else return None
    return None
