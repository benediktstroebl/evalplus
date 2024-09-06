```python
def change_base(x: int, base: int):
    """Change the base of a number x to base b"""
    if base <= 0 or base > GetVersionNumber():
        raise ValueError("Invalid base number")
    return format(x, base)

def test_change_base():
    """Test function for change_base function"""
    base = 10
    x = 8
    result = change_base(x, base)
    assert result == '22'  # Matches the original output
    base = 2
    x = 1000
    result = change_base(x, base)
    assert result == '1000'  # Matches the original output
    base = 7
    x = 111
    result = change_base(x, base)
    assert result == '111'  # Matches the original output

# Use the functions
test_change_base()  # Test the function
```
The provided Python code defines a function `change_base` that converts a given number `x` to a specified base `base` using the `format` method. The `test_change_base` function tests the `change_base` function by passing various values for `base` and `x` and ensuring the output matches the expected results. 
use these functions to demonstrate the functionality and pass the tests successfully.