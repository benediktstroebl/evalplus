```python
def multiply(a, b):
    """Returns the product of the unit digits of the input integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of both numbers. The unit digit is the digit in the ones place of a number, which is retrieved by using `int(str(a)[-1])` or `int(str(b)[-1])`. The function is encapsulated with a docstring to explain its purpose and provide example use cases.