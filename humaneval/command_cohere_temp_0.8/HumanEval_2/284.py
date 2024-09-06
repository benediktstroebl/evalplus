```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. This is done by finding the difference between the given number and the largest integer that is less than or equal to the number, which is achieved by int(number). The int() function converts the number to a integer discarding any digits after the decimal point, effectively leaving only the largest integer less than the original number. The returned integer value is then subtracted from the original number, leaving only the digits after the decimal point. This is the key process in calculating the 'decimal part' of the number in floating-point decimal computations.