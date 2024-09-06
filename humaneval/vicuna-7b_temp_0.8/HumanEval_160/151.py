
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
    operand = list(operand)
    if len(operator) == len(operand) - 1:
        operator = [operator[0]]
    else:
        raise ValueError("The length of operator list is not equal to the length of operand list minus one.")
    for i in range(len(operator)):
        for j in range(len(operand)):
            if operator[i] == '**':
                if i == j:
                    raise ValueError("Exponentiation has to have at least two operands.")
            elif operator[i] == '//':
                if not operand[j] % operand[j+1] % operand[j+2]:
                    raise ValueError("Division by zero is not allowed.")
            else:
                result = 0
                for k in range(len(operand)):
                    result = operand[j] + result * operator[i] * operand[k]
                for k in reversed(range(len(operand))):
                    result = operand[k] - result * operator[i] * operand[k-1]
                for k in range(len(operand)):
                    if operand[k] >= 0:
                        result = result * operator[i] * operand[k]
                return result
    raise ValueError("Invalid algebraic expression.")
