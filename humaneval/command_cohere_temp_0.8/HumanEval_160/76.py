Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result
```
This script provides a Python function called `do_algebra` that takes in two parameters, `operator` and `operand`. It assumes that the length of the `operator` list is equal to the length of the `operand` list minus one. The function returns the result of the algebraic expression formed using the provided operator and operand. It iterates through the `operator` list and accumulates the result by performing the respective operation on each element of the `operand` list. The resulting expression is returned as the sum of the accumulated value.