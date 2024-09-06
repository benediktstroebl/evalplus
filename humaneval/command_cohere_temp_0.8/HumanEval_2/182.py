```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, `number`, and returns the decimal part of the number by subtracting the integer part of the number, obtained using int(), from the input.