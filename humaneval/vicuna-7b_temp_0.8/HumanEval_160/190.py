
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
    # Check if the lists have the same length
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list should have at least one operator and operand list should have at least two operands.")

    # Create a dictionary to store intermediate results
    intermediate_results = {}

    # Evaluate the expression
    for i in range(len(operand)):
        op = operator[i]
        operand_i = operand[i]
        intermediate_result = None
        if op in ['+', '-']:
            intermediate_result = operand_i
        elif op == '/':
            intermediate_result = operand_i
            while intermediate_result % 1 is not 0:
                intermediate_result = intermediate_result // 1
        elif op == '**':
            intermediate_result = operand_i
            while intermediate_result % intermediate_result is not 0:
                intermediate_result = intermediate_result ** 1
        else:
            raise ValueError("Invalid operator: " + str(op))

        # Add intermediate result to the dictionary
        intermediate_results[op] = intermediate_result

    # Return the final result
    return intermediate_results['']