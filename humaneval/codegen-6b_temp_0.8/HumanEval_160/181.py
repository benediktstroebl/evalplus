
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
    #############
    #
    # Write your code here.
    #
    #############
    
    
    def evaluate(op, op_list, val):
        if (op == "+"):
            return op_list[0] + op_list[1]
        elif (op == "-"):
            return op_list[0] - op_list[1]
        elif (op == "*"):
            return op_list[0] * op_list[1]
        elif (op == "/"):
            return op_list[0] // op_list[1]
        elif (op == "**"):
            return op_list[0] ** op_list[1]
        else:
            return op_list[1] ** op_list[0]
    
    def evaluate_helper(op_list, operator, val):
        if (len(op_list) == 1):
            return (val, "")
        else:
            if (len(operator) > 1):
                if (operator[0] == "//"):
                    return (evaluate_helper(op_list[1:], operator[1:], val) * evaluate_helper(op_list[1:], operator[1:], val) // evaluate_helper(op_list[1:], operator[1:], val)[0])
                else:
                    return evaluate_helper(op_list[1:], operator[1:], val) + evaluate_helper(op_list[1:], operator[1:], val)[0]
            else:
                return (val, "")
    
    if (len(operand) == 1):
        return operand[0]
    else:
        return evaluate_helper(operand, operator, operand[0])[1]
