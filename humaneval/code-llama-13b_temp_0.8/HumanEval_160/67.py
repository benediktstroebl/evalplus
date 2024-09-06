
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
    #
    # Note:
    # 1. This is a fairly straightforward problem. Just follow the instructions.
    # 2. Make sure that you have all the necessary components.
    # 3. Use as few additional lists or variables as possible.
    #
    #
    # PLAN:
    # 1. Set up a variable called "result".
    # 2. Iterate through the operator list.
    # 3. Use a for loop to set "first_operand" and "second_operand".
    # 4. Use the "if" statement to evaluate "operator".
    # 5. Set "result" to the necessary value.
    # 6. Return "result" at the end.
    #
    # ANSWER:
    result = operand[0]

    for i in range(len(operator)):
        first_operand = result
        second_operand = operand[i+1]

        if operator[i] == '+':
            result = first_operand + second_operand
        elif operator[i] == '-':
            result = first_operand - second_operand
        elif operator[i] == '*':
            result = first_operand * second_operand
        elif operator[i] == '//':
            result = first_operand // second_operand
        elif operator[i] == '**':
            result = first_operand ** second_operand

    return result
