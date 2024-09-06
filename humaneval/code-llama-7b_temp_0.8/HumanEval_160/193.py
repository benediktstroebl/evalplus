
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
    # check for valid input
    if len(operator) != len(operand)-1:
        return

    # check if there are negative integers in the list
    for i in range(len(operand)):
        if operand[i] < 0:
            return

    # initialize
    current_operand = operand[0]
    temp_operand = []
    temp_operator = []

    for i in range(len(operator)):
        # find a temp operand to multiply
        if current_operand == operand[i]:
            temp_operator.append(operator[i])
            if i != len(operator) - 1:
                temp_operand.append(operand[i+1])
            else:
                break
        else:
            if temp_operator != []:
                # do multiplication
                if temp_operator[-1] == '*':
                    temp_operand = temp_operand[0] * temp_operand[1:]
                    temp_operator.pop()
                elif temp_operator[-1] == '+':
                    temp_operand = temp_operand[0] + temp_operand[1:]
                    temp_operator.pop()
                elif temp_operator[-1] == '-':
                    temp_operand = temp_operand[0] - temp_operand[1:]
                    temp_operator.pop()
                elif temp_operator[-1] == '//':
                    temp_operand = temp_operand[0] // temp_operand[1:]
                    temp_operator.pop()
                elif temp_operator[-1] == '**':
                    temp_operand = temp_operand[0] ** temp_operand[1:]
                    temp_operator.pop()

                # update operand and operator
                if temp_operand != []:
                    operand[i] = temp_operand
                if temp_operator != []:
                    operator[i] = temp_operator

            current_operand = operand[i]

    return operand[-1]
