```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are string must be converted to int
    """
    if not isinstance(base, int):
        raise ValueError("Invalid base number. Input base must be an int.")
    if not isinstance(x, int):
        raise ValueError("Invalid input number.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base number. Input base must be between 2 and 36.")
    return f"{x{base}]{x{base}}"

def test_change_base():
    """
    Test the change_base function.
    """
    expected output: '22'
    x = 8
    base = 3
    result = change_base(x, base)
    assert result == '22'

# Test the function with input validation
try:
    test_change_base()
    assert True
except ValueError as e:
    print(f"Error: {str(e)}")
```