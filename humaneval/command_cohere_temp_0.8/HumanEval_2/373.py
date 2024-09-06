```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. This is done by finding the difference between the number and the closest integer using the in-built int() function which returns the closest integer to the given number.