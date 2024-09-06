
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
    #Initialize a stack to save the operands
    operand_stack = []

    #Append the operator to the stack, after the right operand 
    for element in operator:
        operand_stack.append(element)

    #Append the last operand to the stack
    operand_stack.append(operand[-1])

    #Iterate through the operand list, starting from the second last operand
    for i in range(len(operand)-2, -1, -1):

        #Pop the right operator from the stack and evaluate the expression
        right_op = operand_stack.pop()
        left_op = operand_stack.pop()
        result = do_arithmetic(left_op, right_op, operand[i], operator[i])

        #Append the result to the stack
        operand_stack.append(result)
    
    #The result of the whole expression is the top of the stack
    return operand_stack.pop()
