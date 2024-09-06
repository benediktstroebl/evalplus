```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(54.2) == 0.2
```

This script includes a function, `truncate_number`, that returns the decimal part of a positive floating point number. It does so by taking the difference between the original number and the closest integer, which is obtained using the `round()` function. This ensures that any fractional part of the number is removed, leaving only the decimal portion. 

The included tests assert that the `truncate_number` function returns the expected value for a variety of input scenarios. Each test case evaluates the function with a specific input and compares the result to the expected output. 

You can add more tests to this script to further validate the behavior of the `truncate_number` function for other scenarios.