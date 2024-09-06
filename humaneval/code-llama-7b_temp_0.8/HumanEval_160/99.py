
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

    def get_operator_priority(operator):
        if operator == "*":
            return 1
        elif operator == "/" or operator == "**":
            return 2
        elif operator == "-" or operator == "+":
            return 3

    def do_operations(result, operator, operand):
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "**":
            result = result ** operand
        elif operator == "/":
            result /= operand

        return result

    operations_to_do = []
    result = operand[0]
    operator_index = 0
    for element in operand:
        if operator_index < len(operator) - 1:
            if get_operator_priority(operator[operator_index]) <= get_operator_priority(operator[operator_index + 1]):
                operations_to_do.append(result)
                result = element
                operator_index += 1
            else:
                result = do_operations(result, operator[operator_index], element)
        else:
            operations_to_do.append(result)
            result = do_operations(result, operator[operator_index], element)

    return result

