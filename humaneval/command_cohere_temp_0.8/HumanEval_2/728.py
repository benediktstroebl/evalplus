```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.72) == 0.72
assert truncate_number(123.456) == 0.456
``` 

This script includes a function, `truncate_number`, that returns the decimal part of the input `number`. This is achieved by subtracting the closest integer value from the input number, which inherently includes the decimal part of the float. 

The included tests assert that the function behaves correctly for a few different input types.