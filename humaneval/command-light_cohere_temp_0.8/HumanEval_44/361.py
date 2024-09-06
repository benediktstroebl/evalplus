```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> changebase(8, 2)
    '1000'
    >>> changebase(7, 2)
    '111'
    >>> changebase(1, 16)
    Trace popularized error
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return '{:02}'.format(x)
    elif base == 16:
        return '{:04}'.format(x)
    else:
        raise ValueError("Invalid base number.")
```