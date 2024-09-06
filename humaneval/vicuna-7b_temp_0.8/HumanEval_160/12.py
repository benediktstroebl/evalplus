
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
    operands = list(operand)
    for i in range(len(operand) - 1):
        left_operand = operand[i]
        right_operand = operand[i+1]
        if operator[0] == '**':
            result = left_operand ** right_operand
        elif operator[0] == '//':
            result = left_operand // right_operand
        elif operator[0] == '-':
            result = left_operand - right_operand
        elif operator[0] == '+':
            result = left_operand + right_operand
        else:
            result = operator[1]
            left_operator = operator[0]
            for j in range(len(operator)-1):
                left_operator = operator[j]
                right_operator = operator[j+1]
                if left_operator == '+':
                    result += right_operator
                elif left_operator == '-':
                    result -= right_operator
                elif left_operator == '*':
                    result *= right_operator
                elif left_operator == '**':
                    result **= right_operator
                elif left_operator == '//':
                    result //= right_operator
    return result
