```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    Returns the have string representation after conversion.
    base numbers are open with 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return '{:0{}b}'.format(x, base)
```