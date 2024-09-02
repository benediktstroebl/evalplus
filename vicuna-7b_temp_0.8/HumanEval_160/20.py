
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
    operator_string = operator[1]
    for i in range(len(operands)):
        result = operands[i]
        operator = operator_string
        for j in range(len(operator)):
            if operator[j] == operator[j+1]:
                # remove operator that's already applied
                operator = operator[:j] + operator[j+1:]
            else:
                # calculate the operator
                if operator[j] == '+':
                    result = result + operator[j+1]
                elif operator[j] == '-':
                    result = result - operator[j+1]
                elif operator[j] == '*':
                    result = result * operator[j+1]
                elif operator[j] == '/':
                    result = result // operator[j+1]
                elif operator[j] == '**':
                    result = result ** operator[j+1]
    return result
