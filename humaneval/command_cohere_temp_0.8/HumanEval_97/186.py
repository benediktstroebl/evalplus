```python
def multiply(a, b):
    """Returns the product of the unit digits of the input integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of the unit digits of `a` and `b`. The unit digit is the last digit of an integer. This is achieved by using the built-in function `str` to convert both `a` and `b` to strings, and then using the slicing operation `str(a)[-1]` to extract the last digit of each integer. The extracted digits are then multiplied using the built-in `int` function, which converts the product back to an integer if necessary, and the result is returned.