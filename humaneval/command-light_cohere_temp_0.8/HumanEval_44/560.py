```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are NOTE 10, use it for other bases.
    >>> change_base(8, 45)
    '22'
    """
    # Use built-in int and str conversion
    return str(x, base)

def test_change_base():
    base = 10
    x = int('8')
    assert change_base(x, base) == '22'
    base = 45
    x = int('7')
    assert change_base(x, base) == '22'
    base = 2
    x = int('1000')
    assert change_base(x, base) == '1000'
    base = 7
    x = int('111')
    assert change_base(x, base) == '111'

# Run tests when code is executed
test_change_base()
```
This Python script defines a function `change_base` that converts a given number `x` to a specified base `base`. It also has a function `test_change_base` to check the function's correctness with various test cases.  This also, the test_change_base() function sets a base value, converts an integer to that base, and checks if the result matches the expected output.