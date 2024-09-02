
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
    def eval_algebra(exp):
        def _eval_algebra(exp):
            result = 0
            for i, e in enumerate(exp):
                if i%2 == 0:
                    result += e
                else:
                    result *= e
            return result
        exp.reverse()
        # exp.pop()
        exp = str(exp)
        exp = eval(exp)
        return exp

    def build_exp(op, arr):
        result = []
        i = 1
        for o in op:
            if o == "+":
                result.append(arr[i])
                i += 1
            elif o == "-":
                result.append(arr[i])
                i += 1
            elif o == "*":
                result.append(arr[i])
                i += 1
            elif o == "//":
                result.append(arr[i])
                i += 1
            elif o == "**":
                result.append(arr[i])
                i += 1
        return result

    def build_op(op):
        for i, o in enumerate(op):
            if o == '+':
                op[i] = operator.add
            elif o == '-':
                op[i] = operator.sub
            elif o == '*':
                op[i] = operator.mul
            elif o == '//':
                op[i] = operator.floordiv
            elif o == '**':
                op[i] = operator.pow
        return op

    result = eval_algebra(build_exp(build_op(operator), operand))
    return result

