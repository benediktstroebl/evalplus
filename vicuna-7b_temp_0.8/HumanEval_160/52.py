
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
    operand_count = len(operand)
    operator_count = len(operator)
    if operator_count < operand_count - 1:
        print("Invalid operator list")
        return 0
    else:
        expression = []
        for i in range(0, operand_count, 1):
            expression.append(operator[i])
        for j in range(0, operand_count - 1, 1):
            operand_i = operand[j]
            operand_j = operand[j + 1]
            if expression[j] == '*':
                result = operand_i * operand_j
                if expression[j + 1] == '^':
                    result = result ** int(expression[j + 2])
            elif expression[j] == '/':
                result = operand_i / operand_j
            else:
                result = operand_i
                for k in range(j + 1, operand_count):
                    if expression[k] == '**':
                        result = result ** int(expression[k + 1])
                    else:
                        result = result + operand_j
        return result
