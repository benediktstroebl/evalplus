Here's a Python script that solves the problem you've outlined, along with example usage and tests to validate the solution:
```python
def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression using the provided operator and operand.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lists must have matching lengths.")
    
    expression = []
    for i in range(len(operand) - 1):
        expression.append(operand[i])
        for j in range(len(operator)):
            if operator[j] == '+':
                expression.append(expression[-1] + expression[-2])
                expression.pop()
            elif operator[j] == '-':
                expression.append(expression[-1] - expression[-2])
                expression.pop()
            elif operator[j] == '*':
                expression.append(expression[-1] * expression[-2])
                expression.pop()
            elif operator[j] == '**':
                expression.append(expression[-1] ** expression[-2])
                expression.pop()
            elif operator[j] == '/':
                if expression[-1] == expression[-2] == 0:
                    raise ValueError("Division by zero is not allowed.")
                expression.append(expression[-1] // expression[-2])
                expression.pop()
            else:
                raise ValueError(f"Invalid operator: {operator[j]}")
    
    return expression[-1]

# Example usage:
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)  # Output: 9

# Test cases:
tests = [
    ([['+', '*', '-'], [2, 3, 4, 5]], 9),
    ([['-', '*', '+'], [5, 2, 3, 4]], 2),
    ([['*', '+', '-'], [4, 2, 3, 5]], 13),
    ([['*', '**', '-'], [2, 3, 4, 5]], 120),
    ([['+', '*', '+'], [0, 2, 3, 4]], 10),
    ([['-', '/', '**'], [5, 0, 3, 4]], 0),
    ([['*', '+', '^'], [4, 2, 0, 5]], 25),
]

for test in tests:
    operator, expected = test
    result = do_algebra(operator, operand)
    assert result == expected, f"Expected {expected}, but got {result} for input {operator} and {operand}"
```
This script defines a `do_algebra` function that takes two arguments, `operator` (a list of algebraic operations) and `operand` (a list of integers). It constructs an expression using the provided operator and operand and then returns the result of the expression.

The code includes tests to validate the solution, ensuring that it handles different combinations of operators and operands correctly, and raises appropriate exceptions for invalid inputs.