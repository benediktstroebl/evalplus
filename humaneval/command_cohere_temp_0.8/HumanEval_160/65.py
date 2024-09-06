Here's a Python script that solves the problem you've outlined using a function with the specified parameters:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    assert oper_len == len(operand) - 1, "Operator list length must be equal to operand length - 1"
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result
```
This script defines a function `do_algebra` that takes in two parameters, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists. The function iterates through the lengths of `operator` and `operand`, verifying that the length of the operator list is correct in the process, and accumulates the result by multiplying each element in `operand` with its corresponding element in `operator`. The result is then returned as the final value of the expression.