```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as inputs and returns the product of their unit digits. The unit digit is the digit in the ones place of a number, which is retrieved using the expression `int(str(a)[-1])` for both inputs `a` and `b`. The function is then tested with the example inputs provided in the problem, and the appropriate values are returned.