```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(122.456) == 0.456
```

This script includes a function, `truncate_number`, that returns the decimal part of the input number. It does so by taking the difference between the input number and its closest integer value, which is achieved using the `round` function.

Three test cases are included to validate the function against known outputs. You can use these to verify the correctness of the function.