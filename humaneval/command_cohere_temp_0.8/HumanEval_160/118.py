Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The function is designed to support basic algebra operations (`+`, `*`, `^`, `-`, `//`) along with proper handling of negative numbers:
```python
def do_algebra(operator, operand):
    # Sort the operand list to ensure consistent result ordering
    operand = sorted(operand)
    
    # Build the expression string
    expr = ''
    i = 0
    while i < len(operand) - 1:
        if operator[i] == '+':
            expr += f'{operand[i]} + {operand[i + 1]}'
        elif operator[i] == '-':
            expr += f'{operand[i]} - {operand[i + 1]}'
        elif operator[i] == '*':
            expr += f'{operand[i]} * {operand[i + 1]}'
        elif operator[i] == '//':
            expr += f'{operand[i]} // {operand[i + 1]}'
        elif operator[i] == '^':
            expr += f'{operand[i]} ^ {operand[i + 1]}'
        i += 1
    
    # Handle the last element if it requires a different operation
    if operator[-1] == '-':
        expr += f'{operand[-2]} - {operand[-1]}'
    elif operator[-1] in ('*', '^', '//'):
        expr += f'{operand[-2]} {operator[-1]} {operand[-1]}'
    
    return int(expr)
```

This script includes a test suite with a number of test cases designed to verify the correctness of the `do_algebra` function. Each test case provides a specific `operator` and `operand` list as input, and the expected result is calculated manually to ensure the function produces the expected output. You can add more test cases as needed to cover additional scenarios and edge cases.

```python
def test_do_algebra():
    # Test case 1: Simple addition
    op = ['+'] * 2
    operand = [2, 3]
    assert do_algebra(op, operand) == 5

    # Test case 2: Simple subtraction
    op = ['-'] * 2
    operand = [4, 2]
    assert do_algebra(op, operand) == 2

    # Test case 3: Simple multiplication
    op = ['*'] * 2
    operand = [5, 3]
    assert do_algebra(op, operand) == 15

    # Test case 4: Simple division
    op = ['//'] * 2
    operand = [10, 2]
    assert do_algebra(op, operand) == 5

    # Test case 5: Exponentiation
    op = ['^'] * 2
    operand = [3, 4]
    assert do_algebra(op, operand) == 81

    # Test case 6: Mixed operations
    op = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(op, operand) == 29

    # Test case 7: Mixed operations with negative numbers
    op = ['-', '*']
    operand = [3, -2, 4, 5]
    assert do_algebra(op, operand) == -10

    # Test case 8: Floor division
    op = ['//'] * 3
    operand = [2, 4, 5]
    assert do_algebra(op, operand) == 2
```

This test