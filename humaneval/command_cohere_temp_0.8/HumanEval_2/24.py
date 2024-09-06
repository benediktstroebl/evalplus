```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number.
    """
    return number - int(number)
```

The code directly returns the decimal part of the input number by subtracting the integer part of the number (obtained using `int()` function) from the total number.