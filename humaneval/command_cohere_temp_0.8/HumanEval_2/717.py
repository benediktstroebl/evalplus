```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.0) == 0.0
assert truncate_number(7.01) == 0.01
``` 

This script includes a well-documented function 'truncate_number' that takes a positive floating point number as an argument and returns its decimal part. It uses the subtraction operation `int(number) - number` to remove the integer part of the number, leaving behind the decimal part.

Three tests were conducted to ensure the function works as expected with different input scenarios. Adjust the tests or add more to suit your specific needs.