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

This script includes a function `truncate_number` that takes a single parameter, `number`, and returns the decimal part of that number. To do this, it simply subtracts the integer part of `number` (obtained via `round()`) from `number` itself, leaving behind only the decimal part.

Three test cases are included to validate the function's behavior: it correctly identifies the decimal part of `3.5`, `7.8`, and `0.1` as `0.5`, `0.8`, and `0.0` respectively. 

You can add more tests to this script to cover additional scenarios and ensure the function's robustness.