```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise TypeError("Input values must be integers or floats")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    # convert the given number to the required base
    s = str(x, base)
    return s

# Test function
test_change_base = change_base. test_change_base(8, 3)  # expected output: '22'
test_change_base(8, 2)  # expected output: '1000'
test_change_base(7, 2)  # expected output: '111'
test_change_base(123, 10)  # expected output: '123010'
test_change_base(123456, 2)  # expected output: '234567'
```