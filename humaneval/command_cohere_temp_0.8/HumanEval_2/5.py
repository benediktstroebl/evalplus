```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.72) == 0.72
assert truncate_number(123.456) == 0.456
```

This script includes a function, `truncate_number`, that returns the decimal part of a positive floating point number. It separates the given number by the largest integer part and the remainder (which is always less than 1). It then evaluates the remainder and returns it. The tests assert that the function correctly identifies the decimal part of different input numbers.