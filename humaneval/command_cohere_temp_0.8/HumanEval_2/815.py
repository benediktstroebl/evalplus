```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number, subtracts the closest integer to it (using `int()` function), and returns the result, which is the residual that is always smaller than 1.