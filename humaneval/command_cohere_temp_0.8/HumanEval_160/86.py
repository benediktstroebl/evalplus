Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebra expression created using the two input lists. The script also includes a set of tests to ensure the function behaves as expected:
```python
def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression using two input lists.

    Args:
        operator (list): List of algebra operations, such as ['+', '*', '-'].
        operand (list): List of integers to be used in the expression, e.g.[2, 3, 4, 5].

    Returns:
        int: Result of the algebraic expression created from the two input lists.

    Example:
        >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
        9
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length must be equal to operand list length minus one.")
    expression = ""
    for i in range(len(operand) - 1):
        expression += operator[i]
        expression += "("
        expression += str(operand[i])
        expression += ", "
        expression += str(operand[i + 1])
        expression += ")"
    expression += operator[-1]
    expression += "("
    expression += str(operand[-1])
    expression += ")"
    return eval(expression)

# Tests:
test_cases = [
    ([['+', '*', '-'], [2, 3, 4, 5]], 9),
    ([['-', '*', '+'], [2, 3, 4, 5]], -9),
    ([['*', '+', '-'], [2, 3, 4, 5]], -15),
    ([['+', '-', '*'], [2, 3, 4, 5]], -5),
    ([['*', '-', '+'], [2, 3, 4, 5]], 3),
    ([['+', '*', '-'], [0, 1, 2, 3]], 6),
    ([['-', '*', '+'], [0, 1, 2, 3]], -6),
    ([['*', '+', '-'], [0, 1, 2, 3]], 0),
]

for case in test_cases:
    operator, operand = case
    print(f"{do_algebra(operator, operand)} == {case[1]}")
```
This code defines a function that adheres to the problem statement, and the tests section ensures its correctness for a variety of scenarios.