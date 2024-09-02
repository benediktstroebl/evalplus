
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
    # Create an empty expression
    expression = ""
    
    # Check if operator list is empty
    if len(operator) == 0:
        return "0"
    
    # Get the number of operands in the operand list
    num_operands = len(operand)
    
    # Check if operator list is empty
    if len(operator) == 0:
        return "0"
    
    # Check if operator list has at least one operator
    if len(operator) == 1 and isinstance(operator[0], str):
        # Get the first operand in the operand list
        first_operand = operand[0]
        
        # Evaluate the expression
        result = eval_expression(expression + operator[0] + first_operand)
        
        return result
    else:
        # Get the last operator in the operator list
        last_operator = operator[-1]
        
        # Evaluate the expression
        expression_list = expression + last_operator
        expression_list = eval_expression(expression_list)
        
        # Get the current operand in the operand list
        current_operand = operand[-1]
        
        # Evaluate the expression
        result = eval_expression(expression_list + current_operand)
        
        # Add the operator to the expression
        result = operator[1:len(operator)][0](result, current_operand)
        
        return result
