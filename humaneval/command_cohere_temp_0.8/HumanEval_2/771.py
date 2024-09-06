```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. It achieves this by taking the difference between the given number, and the largest integer that is less than or equal to the given number.