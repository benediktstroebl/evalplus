
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
    operand_len = len(operand)
    operator_len = len(operator) - 1
    expression = []
    result = 0
    for i in range(operand_len):
        for j in range(operator_len):
            if j == 0:
                # Addition
                if operator[j] == '+':
                    expression.append(operand[i])
                    result += expression[-2]
                    expression.pop()
                    expression.pop()
                    break
                elif operator[j] == '-':
                    expression.append(operand[i])
                    result -= expression[-2]
                    expression.pop()
                    expression.pop()
                    break
                elif operator[j] == '*':
                    expression.append(operand[i])
                    result *= expression[-2]
                    expression.pop()
                    expression.pop()
                    break
                elif operator[j] == '**':
                    expression.append(operand[i])
                    result **= expression[-2]
                    expression.pop()
                    expression.pop()
                    break
                elif operator[j] == '//':
                    expression.append(operand[i])
                    result = (result / expression[-2])
                    expression.pop()
                    expression.pop()
                    break
    return result
