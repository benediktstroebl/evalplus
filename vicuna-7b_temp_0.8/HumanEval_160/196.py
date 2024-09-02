
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
    operands = [operand[0]]
    for i in range(1, len(operand)):
        operands.append(operand[i])
    operator_evaluation = []
    for operator in operator:
        if operator == '+':
            operator_evaluation.append(operands.pop(0) + operands[-1])
        elif operator == '-':
            operator_evaluation.append(operands.pop(0) - operands[-1])
        elif operator == '*':
            operator_evaluation.append(operands.pop(0) * operands[-1])
        elif operator == '/':
            if operands[-1] != 0:
                operator_evaluation.append(operands.pop(0) / operands[-1])
            else:
                raise ValueError("Cannot divide by zero")
        elif operator == '**':
            operator_evaluation.append(pow(operands.pop(0), operands[-1]))
        else:
            raise ValueError("Invalid operator")
    result = operator_evaluation[0]
    for i in operator_evaluation[1:]:
        result = operator_evaluation[i] * result ** operator_evaluation[i+1]
    return result
