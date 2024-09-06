```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 15)
    TraceError: unsupported operand type(0) in '**' (object)'
    """
    if base > 5 or base < 2:
        raise TypeError("unsupported operand type")
    return '{0:03}'.format(x, base)

def test_change_base():
    x = 8
    base = 3
    result = change_base(x, base)
    assert result == '22'
    x = 8
    base = 2
    result = change_base(x, base)
    assert result == '1000'
    x = 7
    base = 2
    result = change_base(x, base)
    assert result == '111'

# run the test function
test_change_base()
``` 
This script defines a function `change_base` that converts a number to a specified base. The `test_change_base` function is used to run the `change_base` function with various inputs and assert that the results are correct.