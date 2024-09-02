
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
    operator_actions = list(operator)
    operator_count = len(operator_actions)

    for i in range(0, len(operand), operator_count):
        operator = operator_actions[i:i+1]
        operand = operand[i:i+1]

        if operator == '+':
            result = operand[0]
            for j in range(1, len(operand)):
                result = result + operand[j]
            return result
        elif operator == '-':
            result = operand[0]
            for j in range(1, len(operand)):
                result = result - operand[j]
            return result
        elif operator == '*':
            result = operand[0]
            for j in range(1, len(operand)):
                result = result * operand[j]
            return result
        elif operator == '/':
            if not any(operand[j] > 0 for j in range(1, len(operand))):
                return None
            else:
                result = operand[0]
                for j in range(1, len(operand)):
                    result = result / operand[j]
                return result
        elif operator == '**':
            if not any(operand[j] > 0 for j in range(1, len(operand))):
                return None
            else:
                result = operand[0]
                for j in range(1, len(operand)):
                    result = result ** operand[j]
                return result

    return None
