```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. This is achieved by finding the difference between the number and the nearest integer using the `int()` function which returns the integer part of the number, and then returning the difference, which is the decimal part desired. The function is self-contained and can be run as is. It does not rely on any external dependencies nor extra code to be functional. It also has a useful docstring that describes its purpose and behavior.