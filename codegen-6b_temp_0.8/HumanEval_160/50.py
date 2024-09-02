
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
    index = 0
    if len(operator) == len(operand) - 1:
        add_list = []
        for item in operator:
            if item == '+':
                add_list.append(operand[index])
                add_list.append(operand[index + 1])
                index += 2
            elif item == '*':
                add_list.append(operand[index])
                add_list.append(operand[index + 1])
                add_list.append(operand[index + 2])
                index += 3
            elif item == '-':
                add_list.append(operand[index])
                add_list.append(operand[index + 1])
                add_list.append(-1 * operand[index + 2])
                index += 3
            elif item == '//':
                add_list.append(operand[index])
                add_list.append(operand[index + 1])
                add_list.append(operand[index + 3])
                add_list.append(operand[index + 4])
                index += 5
            elif item == '**':
                add_list.append(operand[index])
                add_list.append(operand[index + 1])
                add_list.append(operand[index + 2])
                add_list.append(operand[index + 3])
                index += 4

        return add_list
