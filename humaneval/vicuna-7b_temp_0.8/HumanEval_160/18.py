
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
    operands = []
    for i in range(len(operand)):
        operands.append(operand[i])

    operator_operands = []
    for i in range(len(operator)):
        operator_operands.append(operator[i][0])
        operator_operands.append(operator[i+1])

    for i in range(len(operator_operands)):
        operator_operands[i] = int(operator_operands[i])

    expression = ""
    for i in range(len(operator_operands)):
        for j in range(len(operand)):
            operation = operator_operands[i]
            operand_index = j
            if operation == '*':
                result = operand[operand_index]
                for k in range(i+1, len(operator_operands)):
                    if operator_operands[k] == '*':
                        result = result * operator_operands[k]
                    elif operator_operands[k] == '/':
                        result = result * (operator_operands[k] // operand_index)
                    else:
                        result = result * operator_operands[k]
                expression += str(result)
            elif operation == '//':
                result = operand[operand_index]
                for k in range(i+1, len(operator_operands)):
                    if operator_operands[k] == '*':
                        result = result * operator_operands[k]
                    elif operator_operands[k] == '/':
                        result = result * operand_index
                    else:
                        result = result * operator_operands[k]
                expression += str(result)
            elif operation == '**':
                result = operand[operand_index]
                for k in range(i+1, len(operator_operands)):
                    result = result * operator_operands[k]
                expression += str(result)
            else:
                expression += str(operand_index)
                if operator_operands[i] == operator_operands[i+1]:
                    expression +=
