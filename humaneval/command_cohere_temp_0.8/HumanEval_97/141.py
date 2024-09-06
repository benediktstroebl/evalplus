```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The code uses the str method to convert the integers to strings and int to convert the unit digits (the last digits) of the strings back to integers, achieving the desired result.