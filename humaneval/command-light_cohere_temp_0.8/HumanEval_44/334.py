```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are string: 'base'
    """
    assert isinstance(x, int)
    assert isinstance(base, int)
    assert base >= 2, f"Base should be greater than 2, got {base}"
    assert x > 0, f"Input x should be positive, got {x}"

    new_str = ''
    for digit in str(x):
        if digit >= base:
            new_str = new_str + str(digit - base) + '0'
        else:
            new_str = new_str + str(digit) + '0'

    return new_str
```