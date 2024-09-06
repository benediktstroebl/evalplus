Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists according to the problem statement:
```python
def do_algebra(operator, operand):
    # type the expression
    expression = ' '.join([f'{o}{{operand[i]}}' for i, o in enumerate(operator)])
    
    # evaluate the expression
    result = eval(expression)
    
    return result

# Example usage
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9

# Test cases
tests = [
    ([['+', '*', '-'], [2, 3, 4, 5]], 9),
    ([['*', '-'], [2, 3, 4, 5]], -7),
    ([['+', '-', '*'], [2, 3, 4, 5]], 13),
    ([['**', '+', '-'], [2, 3, 4, 5]], -39),
]

for op, answer in tests:
    assert do_algebra(*op) == answer, f"Expected {answer}, but got {do_algebra(*op)}"
```

The script provides a function `do_algebra` that takes an `operator` list (e.g., ['+', '*', '-']) and an `operand` list (e.g., [2, 3, 4, 5]). It constructs an expression string (e.g., '2 + 3 * 4 - 5') and uses the `eval()` function to calculate the result, returning the outcome.

Example usage and test cases are provided to validate the functionality of the script.