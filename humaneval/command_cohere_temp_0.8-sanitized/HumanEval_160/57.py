def do_algebra(operator, operand):
    """
    Evaluates an algebraic expression using provided operators and integers.

    :param operator: List of algebraic operations containing '+' for addition, 
                    '-' for subtraction, '*' for multiplication, '//' for floor division
                    and '**' for exponentiation.
    :param operand: List of integers to be used in the expression.
    :return: Evaluated expression using the given operators and integers.
    """
    # Ensure the lengths of the operator and operand lists are as required.
    assert len(operator) == len(operand) - 1
    assert len(operand) >= 2

    # Use recursion to build and evaluate the expression.
    def eval_expr(idx):
        if idx == len(operand):
            return operand[-1]
        else:
            operator_idx = idx % len(operator)
            next_idx = (idx + 1) % len(operand)
            return operator[operator_idx](eval_expr(next_idx), eval_expr(next_idx))

    return eval_expr(0)