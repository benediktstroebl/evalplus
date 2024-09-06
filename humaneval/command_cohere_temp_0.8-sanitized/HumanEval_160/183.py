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
    size_diff = len(operator) - len(operand) + 1
    assert size_diff >= 1, "operator list must have the same size as operand list minus one element"
    assert all(op in ['+', '-', '*', '**', '//'] for op in operator), "operator list must contain only valid algebra operations"
    assert all(op >= 0 for op in operand), "operand list must contain only positive integers"

    terms = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            term = operand[i]
            for k in range(len(operator)):
                if operator[k] == '+':
                    term += operand[j]
                if operator[k] == '-':
                    term -= operand[j]
                if operator[k] == '*':
                    term *= operand[j]
                if operator[k] == '**':
                    term **= operand[j]
                if operator[k] == '//':
                    term //= operand[j]
                terms.append(term)
    return terms[0]