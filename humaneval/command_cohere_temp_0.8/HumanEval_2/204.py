```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter into an integer using `int()` and then returns the difference between the original number and the integer to get the decimal part of the number.