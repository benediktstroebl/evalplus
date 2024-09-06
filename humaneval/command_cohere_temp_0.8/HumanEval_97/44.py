```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts their unit digits (the last digit of their string representations) using `str(a)[-1]` and `str(b)[-1]`, respectively, and returns their product as an integer. This approach utilizes string manipulation to efficiently determine the unit digits, resulting in a concise solution.