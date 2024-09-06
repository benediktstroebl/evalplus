```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    """
    return string representation after conversion
    """
    if x < 0:
        raise ValueError("Input number should be positive")
    return format(x, base)

# Testing function
def test_change_base():
    base = 10
    x = 8
    result = change_base(x, base)
    assert result == '22'
    base = 2
    x = 1000
    result = change_base(x, base)
    assert result == '1000'
    base = 7
    x = 111
    result = change_base(x, base)
    assert result == '111'

# Example usage
test_change_base()
```
This code provides a self-contained function `change_base` that converts a given number `x` to a specified base `base` using the `format()` method. The function also includes input validation to ensure that the input number is positive. 

The `test_change_base()` function tests the `change_base` function with various input combinations and verifies that the output is correct.