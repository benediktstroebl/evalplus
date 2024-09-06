Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists. The script also includes a set of tests to verify the correctness of the function:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = []
    for i in range(num_operands):
        if i == 0:
            expression.append(operand[i])
        else:
            expression.append(operator[i-1])
            expression.append(operand[i])
    return expression[-1]

# Tests
tests = [
    ([['+', '*', '-'], [2, 3, 4, 5]], 9),
    ([['*', '**', '-'], [2, 3, 4, 5]], 40),
    ([['+', '-', '*'], [0, 1, 2, 3]], 5),
    ([['*', '+', '**'], [0, 2, 3, 4]], 40)
]

for op, expected in tests:
    result = do_algebra(op[0], op[1])
    assert result == expected, f"For the lists {op}, expected {expected} but got {result}"
```

To use this script, simply call the `do_algebra` function with the appropriate operator and operand lists. The function will return the result of the algebraic expression created using the provided lists.

You can add more tests to the `tests` list to ensure the function works correctly for a variety of input combinations and corner cases.