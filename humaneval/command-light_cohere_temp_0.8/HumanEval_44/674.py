```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    return string representation after conversion.
    base numbers must 10.
    >>> change_base(8, 3) # result: '22'
    >>> change_base(8, 2) # result: '1000'
    >>> change_base(7, 2) # result: '111'
    """
    if base == 10:
        return str(x)
    else:
        return "{:0b}".format(x, base)
```