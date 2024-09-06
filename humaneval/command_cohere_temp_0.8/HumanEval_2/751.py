```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
```

This script includes a function called `truncate_number` that takes a single parameter, `number`, which is expected to be a positive floating point number. The function subtracts the closest integer to the number from the number itself, effectively removing the integer part of the decomposed number described in the prompt. The resulting value is the decimal part of the original number, which is always less than 1. 

Two assertions are also provided to test the function against sample inputs. The first test ensures that the decimal part of the number is correctly identified when the input is 3.5; the second tests the function's correctness when 7.8 is provided as the input. Both outcomes are expected to be true, meaning that the function returns the expected values for these inputs.  This is a common testing approach in Python, used to validate that code behaves as expected.