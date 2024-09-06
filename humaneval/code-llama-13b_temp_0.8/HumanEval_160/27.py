
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
    #Initialize variable.
    i = 0
    j = 1

    #For loop to evaluate the expression.
    while i < len(operator):
        if operator[i] == '+':
            operand[j-1] += operand[j]
            del operand[j]
            del operator[i]

        elif operator[i] == '-':
            operand[j-1] -= operand[j]
            del operand[j]
            del operator[i]

        elif operator[i] == '*':
            operand[j-1] *= operand[j]
            del operand[j]
            del operator[i]

        elif operator[i] == '//':
            operand[j-1] = operand[j-1] // operand[j]
            del operand[j]
            del operator[i]

        elif operator[i] == '**':
            operand[j-1] = operand[j-1] ** operand[j]
            del operand[j]
            del operator[i]
        
        else:
            print("The operator list has invalid operator.")

        i += 1
        j += 1

    #Return result.
    return operand[0]
