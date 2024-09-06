Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly, as it needs to be iterated through differently
    if "**" in operator:
        for i in range(len(operand)):
            result += operand[i] ** operator.index("**")
        return result
    # Handle other operations through recursive multiplication
    for i in range(len(operand)):
        result += operand[i] * do_algebra(operator, operand[i:])
    return result
```

The function works by recursively breaking down the algebraic expression into basic operations, and then performing these operations in a recursive fashion. The exponentiation operation is explicitly handled due to its uniqueness in arithmetic operations. The other operations are handled by breaking down the algebraic expression into smaller sub-expressions through recursive multiplication. The function ultimately returns the result of the evaluation of the algebraic expression.