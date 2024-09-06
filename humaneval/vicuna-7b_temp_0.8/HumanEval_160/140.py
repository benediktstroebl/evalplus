
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
    # Check if operator list has at least one operator
    if len(operator) < 1:
        return 0

    # Check if operand list has at least two operands
    if len(operand) < 2:
        return 0

    # Get the first operator in operator list
    op1 = operator[0]

    # Get the first operand in operand list
    op2 = operand[0]

    # Create a list to store the results
    results = []

    # Evaluate the expression by repeatedly applying the operator to the operands and storing the result
    # in the list
    for i in range(len(operator)):
        # Get the next operator in operator list
        op3 = operator[i]

        # Get the next operand in operand list
        op4 = operand[i]

        # Check if the operator is an addition or subtraction
        if op3 == '+':
            # If the operator is addition, add the result of the previous expression and the operand
            # and append the result to the list
            results.append(op1 + op4)

        elif op3 == '-':
            # If the operator is subtraction, subtract the result of the previous expression from the operand
            # and append the result to the list
            results.append(op1 - op4)

        # Check if the operator is multiplication or exponentiation
        elif op3 == '*':
            # If the operator is multiplication, multiply the result of the previous expression and the operand
            # and append the result to the list
            results.append(op1 * op4)

        elif op3 == '**':
            # If the operator is exponentiation, raise the result of the previous expression to the power
            # specified in the operand and append the result to the list
            results.append(op1 ** int(op4))

        # Check if the operator is a floor division or a subtraction
        elif op3 == '/':
            # If the operator is a floor division, divide the result of the previous expression by the operand
            # and append the quotient to the list
            results.append(np.floor(op1 /
