```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10 or most common bases.
    >>> change_base(8, 3)
    '22'
    """
    return '{:02}'.format(x, base)

def test_change_base():
    """Test the change_base function"""
    assert change_base(8, 3) == '22'
    assert change_base(5, 4) == '401'
    assert change_base(123, 5) == '55555'
    assert change_base(0, 9) == '9999'
    assert change_base(10, 10) == '1010'

# Call the test function
test_change_base()
```