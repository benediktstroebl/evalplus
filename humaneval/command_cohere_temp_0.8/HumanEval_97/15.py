```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of their unit digits. The unit digit is the digit in the ones place of a number, which is retrieved using the expression `int(str(a)[-1])` for both inputs. The returned product is then computed simply by multiplying these two unit digits. This solution assumes that the input is valid and the integers are strictly positive.