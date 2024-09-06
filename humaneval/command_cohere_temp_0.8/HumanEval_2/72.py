```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.777) == 0.777
```

This script includes a function, `truncate_number`, that returns the decimal part of a positive floating point number. It achieves this by subtracting the integer part of the number (obtained using Python's `int()` function) from the original number, resulting in the leftover decimal part. 

The provided tests validate the function's behavior for different input numbers, ensuring that it returns the intended decimal part for both whole and decimal portions of the number.