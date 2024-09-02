
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
    expression = []
    for i in range(len(operand) - 1):
        left = operand[i]
        right = operand[i + 1]
        operator_index = operator.index(operator[i])
        operator_value = operator[operator_index]

        # Addition
        if operator_value == '+':
            expression.append(left)
            expression.append(right)
            result = expression.pop()
            result = result * result
            expression.pop()
            expression.pop()

        # Subtraction
        elif operator_value == '-':
            expression.append(right)
            expression.append(left)
            result = expression.pop()
            result = result * result
            expression.pop()
            expression.pop()

        # Multiplication
        elif operator_value == '*':
            expression.append(right)
            expression.append(left)
            result = expression.pop()
            result = result * result
            expression.pop()
            expression.pop()

        # Floor division
        elif operator_value == '//':
            expression.append(right)
            expression.append(left)
            result = expression.pop()
            result = result * result
            expression.pop()
            result = result / operand[i + 1]

        # Exponentiation
        elif operator_value == '**':
            expression.append(right)
            result = result * result
            expression.pop()

    return result
