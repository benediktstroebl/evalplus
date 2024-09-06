```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float to an integer and subtracts the result from the original number, leaving you with just the decimal portion.