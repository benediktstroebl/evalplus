
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
    operand = [int(i) for i in operand]
    left = operand[0]
    right = operand[1]
    operator_idx = 0
    operator_stack = deque()
    for i in operator:
        if operator[i] == '*':
            operator_stack.append(operator[i])
            operator_idx += 1
        elif operator[i] == '/':
            operator_stack.append(operator[i])
            operator_idx += 1
        elif operator[i] == '//':
            operator_stack.append(operator[i])
            operator_idx += 1
        elif operator[i] == '-':
            operator_stack.append(operator[i])
            operator_idx += 1
        elif operator[i] == '+':
            operator_stack.append(operator[i])
            operator_idx += 1
    while operator_stack:
        op = operator_stack.popleft()
        if op == '*':
            result = right * left
            if operator_idx > 0:
                for j in range(0, operator_idx - 1, 1):
                    right = right * operand[1]
                if operator_idx > 1:
                    for j in range(1, operator_idx - 1, 1):
                        left = left * operand[1]
                else:
                    for j in range(1, operator_idx - 1):
                        left = left * operand[1]
        elif op == '/':
            result = right / left
            if operator_idx > 0:
                for j in range(0, operator_idx - 1, 1):
                    right = right * operand[1]
                if operator_idx > 1:
                    for j in range(1, operator_idx - 1, 1):
                        left = left * operand[1]
                else:
                    for j in range(1, operator_idx - 1):
                        left = left * operand[1]
        elif op == '//':
            result = right // left
            if operator_idx > 
