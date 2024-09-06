Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The function is designed to support basic algebra operations (`+`, `-`, `*`, `//`, `**`) and returns the result of the computation. 

The script also includes a set of tests to validate the function against different combinations of operators and operands to ensure its functionality. 

```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
        for j in range(i + 1, num_operands):
            if operator[i] == "+":
                expr.append(operand[j])
            elif operator[i] == "-":
                expr.append(operator[i] + "(" + operand[j] + " - " + operand[i] + ")")
            elif operator[i] == "*":
                expr.append(operator[i] + "(" + operand[j] + " * " + operand[i] + ")")
            elif operator[i] == "//":
                expr.append(operator[i] + "(" + operand[j] + " // " + operand[i] + ")")
            elif operator[i] == "**":
                expr.append(operator[i] + "(" + operand[j] + " ** " + operand[i] + ")")
    return expr[0] + " " + expr[1:]

# Tests
operator_list = ['+', '*', '-', '//', '**']
operand_list = [2, 3, 4, 5]
test_cases = [
    (operator_list, operand_list, 9),
    (['+', '*', '-'], [2, 3, 4, 5, 6], 12),
    (['**', '+'], [2, 3, 4], 24),
    (['*', '**', '-'], [2, 3, 4, 5], -80),
    (['//', '**', '+'], [1, 2, 3], 1),
    (['+', '**', '-'], [2, 3, 4, 0], 0),
]

for operator, operand, expected in test_cases:
    actual = do_algebra(operator, operand)
    assert actual == expected and isinstance(actual, int), f"Expected {expected} but got {actual}"
```

To use the `do_algebra` function, you can call it by providing the `operator` and `operand` lists as arguments like this:
```python
result = do_algebra(operator_list, operand_list)
print(result)
```

To run the tests, you can use the `assert` statement to check if the actual result of the algebraic expression matches the expected result for each test case.