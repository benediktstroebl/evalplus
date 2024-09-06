
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
    if (len(operator) != len(operand)-1):
        raise Exception("Operator list is not equal to operand list minus one.")
    elif (len(operator) == 0 or len(operand) == 0):
        raise Exception("Operator or operand list has no value.")
    elif (len(operator) > len(operand)):
        raise Exception("Operator list is greater than operand list.")
    else:
        x = 0
        result = operand[0]
        for i in range(len(operator)):
            if (operator[i] == '+'):
                result += operand[i+1]
            elif (operator[i] == '-'):
                result -= operand[i+1]
            elif (operator[i] == '*'):
                result *= operand[i+1]
            elif (operator[i] == '//'):
                result //= operand[i+1]
            elif (operator[i] == '**'):
                result = int(result**operand[i+1])
            x += 1
        return result
