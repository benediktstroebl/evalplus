```python
def change_base(x: int, base: int):
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
    >>> change_base(123, 5)
    TraceError: None: unsupported operand type(123)
    """
    if base > 0 and base <= 36:
        return f"{x:d}{base}")
    else:
        raise ValueError("Invalid base number")
```