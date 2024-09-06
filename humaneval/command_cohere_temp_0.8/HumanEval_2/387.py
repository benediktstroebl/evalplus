```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function simply subtracts the integer part of the number leaving behind the decimal part of the number.