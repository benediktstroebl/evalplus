
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
    # Check the length of operator and operand
    if len(operator) != len(operand)-1:
        return "Operator length is not equal to operand length minus one"
    if not all(op in ['-', '*', '/'] for op in operator):
        return "Operator must have at least one operator from the set (-, *, /)"

    # Check the length of operand
    if len(operand) == 0:
        return "Operand is empty"

    # Create empty result list
    result = []
    for i in range(len(operand)):
        # Create empty sublist for each operand
        sublist = []
        for j in range(len(operator)-1):
            sublist.append(operator[j])
        sublist.append(operand[i])
        # Append the sublist to result
        result.append(sublist)

    # Create empty expression
    expression = []
    # If the operator is not divisibility operator, append the expression to result
    if operator[0] != 'div':
        for i in range(len(result)):
            if operator[0] == '*':
                expression.append(''.join(map(str, result[i])))
            elif operator[0] == '/':
                expression.append(int(''.join(map(str, result[i]))))
            else:
                expression.append(int(operator[0]) * eval(expression[i]) + eval(operator[1]))
    else:
        # Create empty sublist for divisor
        divisor = []
        # Append the expression to sublist
        for i in range(len(result)):
            if operator[0] == '*':
                expression.append(eval(operator[1]) * eval(expression[i]) + eval(operator[2]))
            elif operator[0] == '/':
                expression.append(int(eval(operator[1]) * eval(expression[i])) / eval(operator[2]))
            else:
                expression.append(eval(operator[1]) * eval(expression[i]) + eval(operator[0]))
        # Append the divisor to expression
        expression.append(''.join(
