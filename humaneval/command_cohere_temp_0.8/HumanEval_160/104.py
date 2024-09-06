Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Remove trailing underscore to avoid deprecation warning in Python 3.8+
    for i in range(len(operand)-1):
        result += operator[i] * operand[i+1]
    return result
```
This script defines a function `do_algebra` that takes in two lists, `operator` and `operand`, and returns the result of the algebraic expression formed using the given operations and integers. The function iterates through the lists, using the elements in `operator` and `operand` to build an expression, then returns the result of this expression. This solution is concise and straightforward.