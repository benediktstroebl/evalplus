```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers <= 2 allowed.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '100'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 3)
    TraceError: incompatible types: int() required, got 'str'
    """
    if base > 2:
        raise ValueError("base number is too big")
        
    return '{:0b}'.format(x, base)
```