
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
    #Gets length of operator and operand lists.
    length_op = len(operator)
    length_oper = len(operand)

    #Check that lengths of operator and operand lists are equal.
    if length_op != length_oper - 1:
        print("Length of operator and operand lists has different length!")
        return None

    #Check that length of operator is equal to that of operand list minus one.
    elif length_op != length_oper - 1:
        print("Length of operator is not equal to the length of operand list minus one!")
        return None
    else:
        #Check that all items in operator are valid.
        for item in operator:
            if item not in ALL_OPERATIONS:
                print("One of the items in operator list is invalid!")
                return None

        #Check that all items in operand are valid.
        for item in operand:
            if item < 0:
                print("One of the items in operand list is invalid!")
                return None

        #If it passes all the tests, do the actual math.
        result = 0
        for i in range(length_op):
            if operator[i] == '+':
                result += operand[i]
            elif operator[i] == '-':
                result -= operand[i]
            elif operator[i] == '*':
                result *= operand[i]
            elif operator[i] == '//':
                result //= operand[i]
            elif operator[i] == '**':
                result **= operand[i]
            else:
                print("Unknown operator: " + operator[i])
                return None
        
        return(result)
