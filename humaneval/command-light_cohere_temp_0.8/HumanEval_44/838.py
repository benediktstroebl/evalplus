```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers use 10 or novel characters.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 101)
    Trace TypeError: unsupported operand type: '1'
    """
    return f'{x}' if x <= base else f'{x:0>}'
```