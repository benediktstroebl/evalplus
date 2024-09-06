
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
    operator = operator.split(',')
    operand = operand.split(',')

    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list and operand list should have the same number of elements")

    for i in range(len(operator)):
        operator_index = int(operator[i])
        operand_index = int(operand[i])
        operator_value = operator_index - 1
        operator_type = "**"
        if 0 <= operator_index <= 25:
            operator_type = "*"
        elif operator_index == 26:
            operator_type = "/"
        elif operator_index == 27:
            operator_type = "**"
        operator = operator[:operator_index]
        operand = operand[:operand_index]
        expression = ""
        for j in range(len(operator)):
            expression += str(operator[j])
            if operator_index == 26:
                expression += str(operand[j])
            elif operator_index == 27:
                expression += str(operand[j])
            elif j < len(operator) - 1:
                expression += str(operator[j])

        result = eval(expression)

        if operator_type == "**":
            result = pow(result, eval(operand[len(operand) - 1]))

        print(str(operator_type) + " " + str(operand_index) + " " + str(operator_value) + " " + str(result))
        print(eval(expression))

    return 0
