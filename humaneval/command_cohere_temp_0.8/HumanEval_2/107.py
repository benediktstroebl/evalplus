```python
def truncate_number(number):
    """ Returns the decimal part of the number """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(122.456) == 0.456
``` 

This script defines a function `truncate_number` that takes in a float as an input and returns the decimal part of the number. This is done by subtracting the integer part of the number (obtained through rounding) from the total number. 

The script also includes tests that check the function for 3 specific cases. The `assert` statements will check if the answer is correct, and  if all the tests pass, there will be an indication at the end that all tests have passed.