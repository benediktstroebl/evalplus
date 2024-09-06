```python
def multiply(a, b):
    """Returns the product of the unit digits of the input integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts their unit digits (i.e., the last digit in their string representation) using `str(a)[-1]` and `str(b)[-1]`, respectively, and returns their product as an integer. This approach utilizes string manipulation to capture and multiply the unit digits, achieving the desired result.