```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by converting the float into an integer). This operation ensures that the result is a float that is smaller than 1, representing the decimal portion of the original number.