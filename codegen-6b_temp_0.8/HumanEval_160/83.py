
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
    result = None

    # XoRtErr #
    if not isinstance(operator, list):
        raise TypeError("operator should be a list")
    if not isinstance(operand, list):
        raise TypeError("operand should be a list")
    if len(operator) < 2 or len(operand) < 2:
        raise ValueError("operator and operand must be lists of at least two elements")

    # Parse operator list into a dictionary
    operator_dict = dict()
    # For operator list, each element of the list is a list of two elements
    for i in range(0, len(operator), 2):
        operator_dict[operator[i]] = operator[i+1]

    # Process operand list, build a result list
    # for each element in the operand list, recursively call the do_algebra() function
    # each result in the result list is the sum of the result list from every element
    result_list = []
    for elem in operand:
        result_list.append(do_algebra(operator_dict, elem))

    # Calculate the result
    if operator_dict['/']:
        result = str(result_list[0]) + operator_dict['/'] + str(result_list[1])
        return float(result)
    else:
        result = result_list[0]
        return result
