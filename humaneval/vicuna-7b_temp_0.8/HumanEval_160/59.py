
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
    operands = operand[:-1]
    if len(operator) == 0:
        return 0
    operator_index = 0
    for i in range(len(operator)):
        if operator[i] == '*':
            product = 1
            for j in range(i+1, len(operator)):
                product *= operands[j]
            product *= operands[-1]
            return product * (operator[i+1] in ['/', '**'])
        elif operator[i] == '/':
            quotient = 1
            for j in range(i+1, len(operator)):
                quotient *= operands[j]
                if operator[i+1] == '/':
                    quotient *= operands[-1]
                elif operator[i+1] == '**':
                    quotient *= operands[-1]
                    return pow(quotient, operator[i+2])
            return quotient * operands[-1]
        elif operator[i] == '**':
            exponent = 1
            for j in range(i+1, len(operator)):
                exponent *= operands[j]
            return pow(exponent, operator[i+1])
        elif operator[i] == '-':
            subtraction = operands[-1]
            for j in range(i-1, -1, -1):
                subtraction *= operands[j]
            return subtraction
        else:
            if operator[i] == operand[0]:
                operands.pop(0)
                break
            else:
                raise ValueError("Invalid operator: " + operator[i])
    return 0
