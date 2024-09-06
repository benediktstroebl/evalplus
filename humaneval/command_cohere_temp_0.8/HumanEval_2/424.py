```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(0.1) == 0.0
```

This script includes a function, `truncate_number`, that returns the decimal part of the input number. It does so by taking the difference between the input number and the closest integer (rounded version of the input number).

The included tests assert that the function behaves as expected for a few different input scenarios. 

Let me know if you would like me to explain any part of the code in more detail.