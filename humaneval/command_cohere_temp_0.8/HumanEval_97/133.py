```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments and returns the product of the unit digits of each number. The unit digit is the digit at the far right of the number (i.e., the digit at position `len(str(num)) - 1`). The function extracts the last digit of each number using `int(str(a)[-1])` and `int(str(b)[-1])`, then returns the product of these extracted digits, providing the result as an integer.