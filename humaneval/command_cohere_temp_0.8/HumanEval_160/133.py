Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebra expression created using the two input lists. The script also includes a set of tests to verify the function works correctly:
```python
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
    num_operands = len(operand)
    expr_list = [operand[i] for i in range(num_operands - 1)]
    for i in range(num_operands - 1):
        operator_token = operator[i % len(operator)]
        if operator_token == '*':
            expr_list.append(expr_list[i] * expr_list[i + 1])
        elif operator_token == '+':
            expr_list.append(expr_list[i] + expr_list[i + 1])
        elif operator_token == '-':
            expr_list.append(expr_list[i] - expr_list[i + 1])
        elif operator_token == '**':
            expr_list.append(expr_list[i] * expr_list[i + 1])
        elif operator_token == '/':
            expr_list.append(expr_list[i] // expr_list[i + 1])
    return expr_list[-1]

# Tests
tests = [([['+', '*'], [2, 3, 4, 5]], 9),
        (['*', '/'], [5, 2, 3, 4]),
        (['+', '-', '*'], [2, 3, 4, 5]),
        (['+', '-', '*', '/'], [0, 1, 2, 3])]

for t in tests:
    test_op, test_res = t
    assert do_algebra(*test_op) == test_res
```

This code defines a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The function uses the `expr_list` variable to build the expression by iterating through the `operator` list and using the respective operator to perform an operation on the two subsequent elements of the `operand` list. The result is the last element in the `expr_list`. The tests are a list of test cases, each containing the `operator` and `operand` inputs for the function and the expected output. Then, the code runs `do_algebra` function on the test cases and compares the output with the expected result using the `assert` statement.  If the computation is incorrect, Python will throw an error and the test will fail, indicating that the function does not provide the expected result.  This approach allows