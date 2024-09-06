```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a number as an input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer that is less than or equal to the given number, which is obtained by converting the number to an integer.