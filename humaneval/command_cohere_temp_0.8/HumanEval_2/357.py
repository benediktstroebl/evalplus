```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` takes a single parameter, `number`, which is a floating-point number. It returns the decimal part of the number by subtracting the integer part of the number (obtained using `int()` function) from the original number. This effectively isolates the decimal part and returns it as the result.  This is the essence of the prompt's requested function.