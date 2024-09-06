```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns the string representation after conversion.
    base numbers less 10
    use a decimal, binary, octal, or hexadecimal number system.
    >>> change_base(8, 3)  # returns '22'
    """
    return format(x, base)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(7, 16) == '33321'
    assert change_base(42, 10) == '4200'
    assert change_base(-42, 2) == '-2147483648'

print("Change base function works correctly!")
```