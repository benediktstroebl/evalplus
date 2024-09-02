
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

    def _do_algebra(operator_list, operand_list):
        if len(operator_list) == 0:
            return int(operand_list[0])
        result = _do_algebra(operator_list[:-1], operand_list[1:])
        if operator_list[-1] == '+':
            return result + operand_list[0]
        if operator_list[-1] == '-':
            return result - operand_list[0]
        if operator_list[-1] == '*':
            return result * operand_list[0]
        if operator_list[-1] == '//':
            return result // operand_list[0]
        if operator_list[-1] == '**':
            return result ** operand_list[0]
        if operator_list[-1] == '|':
            return int(result & operand_list[0])
        if operator_list[-1] == '&':
            return int(result | operand_list[0])
        if operator_list[-1] == '^':
            return result ^ operand_list[0]

    return _do_algebra(operator, operand)

