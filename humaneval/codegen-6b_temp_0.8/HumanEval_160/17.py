
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
    # Equation: result = operator_1 + operator_2 * operand_1
    
    # result = operator_1 + operator_2
    if len(operator) == 1:
        return operator[0] * operand[1]
    
    # result = operator_1 + operator_2 * operator_3
    elif len(operator) == 2:
        result = operator[0] + operator[1] * operand[1]
        
        # Equation: result = operator_4 + operator_5 * operator_6
        if len(operator) == 3:
            result = result + operator[2] * operand[2]
    
    # Equation: result = operator_7 + operator_8 * operator_9
    elif len(operator) == 3:
        result = result + operator[0] + operator[1] * operand[1] + operator[2] * operand[2]
    
    # Equation: result = operator_10 + operator_11 * operator_12 * operator_13
    elif len(operator) == 4:
        result = result + operator[0] + operator[1] * operand[1] + operator[2] * operand[2] + operator[3] * operand[3]

    # Equation: result = operator_14 + operator_15 * operator_16 * operator_17
    elif len(operator) == 5:
        result = result + operator[0] + operator[1] * operand[1] + operator[2] * operand[2] + operator[3] * operand[3] + operator[4] * operand[4]

    # Equation: result = operator_18 + operator_19 * operator_20 * operator_21 * operator_22 + operator_23 * operator_24 * operator_25
    elif len(operator) == 6:
        result = result + operator[0] + operator[1] * operand[1] + operator[2] * operand[2] + operator[3] * operand[3] + operator[4] * operand[4] + operator[5] * operand[5]

    # Equation: result = operator_26 + operator_27