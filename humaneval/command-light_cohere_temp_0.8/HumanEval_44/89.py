```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    Returns the string representation after conversion.
    base numbers 10 and
    to base 2, 10, and 2^6.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 10)
    '88'
    >>> change_base(8, 2)
    '248'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 2)
    TraceError: unsupported operand type(123)
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return str(2 ** (x // 2)) + str(x % 2)
    else:
        raise TypeError("Unsupported operand type!")
```