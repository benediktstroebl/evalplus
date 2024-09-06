```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 20)
    TraceTypeError: unsupported operand type(1) for +()
    """
    if base == 10:
        return str(x)
    elif base < 2 or base > 36:
        raise TypeError("unsupported operand type")
    else:
        return '{:0b}'.format(x, base)
```