
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
    # Create a new list to store the result
    result = []
    # Find the operator for which the operand is the first operand
    for i in range(len(operand) - 1):
        if operand[i] == operand[i + 1]:
            # If the operand is the first operand for the operator
            if operator[0] == operator[1]:
                # If the operator is the second operator
                if operator[1] == '**':
                    # If the operand is the first operand for the exponentiation operator
                    if operator[2] == '*':
                        # If the first operand is negative
                        if operator[3] == '-':
                            # If the second operand is positive
                            if operand[i + 2] > 0:
                                # If the first operand is less than the second operand
                                if operand[i] < operand[i + 2]:
                                    # If the first operand is equal to the second operand
                                    if operand[i] == operand[i + 2]:
                                        # Evaluate the expression
                                        result = eval(operator[3]) ** eval(operator[2])
                                        return result
                    else:
                        # If the first operand is negative
                        if operator[3] == '-':
                            # If the second operand is positive
                            if operand[i + 2] > 0:
                                # If the first operand is less than the second operand
                                if operand[i] < operand[i + 2]:
                                    # If the first operand is equal to the second operand
                                    if operand[i] == operand[i + 2]:
                                        # Evaluate the expression
                                        result = eval(operator[2]) ** eval(operator[3])
                                        return result
                    else:
                        # If the first operand is negative
                        if operator[3] == '-':
                            # If the second operand is positive
                            if operand[i + 2] > 0:
                               
