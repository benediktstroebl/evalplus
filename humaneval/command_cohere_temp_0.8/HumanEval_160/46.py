Here's a Python script that solves the problem you've outlined using a function with the specified parameters:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operator[i] * operand[i]
    return result
```
This script defines a function `do_algebra` that takes in two parameters, `operator` and `operand`, and returns the result of the algebraic expression formed using the two lists. The function loops through the lengths of `operator` and `operand`, using the ith operator from `operator` on the ith number from `operand`, summing them up in the `result` variable. The resulting expression is then returned. 

Note that this script assumes that the lengths of both the `operator` and `operand` lists are at least 1 and that the `operand` list contains at least 2 integers.