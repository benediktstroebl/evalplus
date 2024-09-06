```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(0.1) == 0.0
assert truncate_number(44.0) == 0.0
``` 

This script includes a test suite with several test cases to ensure the `truncate_number` function operates as expected.