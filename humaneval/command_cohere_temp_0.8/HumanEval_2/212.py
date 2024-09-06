```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.0) == 0.0
assert truncate_number(44.01) == 0.01
``` 
In the code snippet above, the `truncate_number` function takes a single parameter `number` which is used to return the decimal part of the positive floating point number. It does so by simply subtracting the closest integer to the number (`int(number)`) from the input `number`, and the result is the residual fractional part of the number.

The tests provided earlier ensure that the function behaves as expected on a few different scenarios. You can further augment the test suite to cover more scenarios like negative numbers, zeros, and numbers with multiple digits after the decimal point, ensuring the function's correctness across a broader spectrum of inputs.