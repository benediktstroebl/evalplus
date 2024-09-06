Here's a Python script that solves the problem you've described using a function with the specified constraints:
```python
def do_algebra(operator, operand):
    result = 0
    # Use tuple unpacking to assign operator and operand to multiple variables
    ((a, b), op, *rest_op) = ((operator[0], operand[0]), operator[1], operator[2:])
    for n in operand[1:]:
        result += a * n * op(b, n)
        a, b = b, n
    for op in rest_op:
        result += a * op(b, operand[-1])
    return result
```

This code defines a function `do_algebra` that takes in two parameters, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The function uses tuple unpacking to assign the elements of `operator` and `operand` to multiple variables. It then loops through the `operand` list, using the `operator` list to build the expression and accumulate the result. Finally, the function returns the calculated result.