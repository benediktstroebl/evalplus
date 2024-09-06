```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Returns the string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 10)
    '100000000'
    >>> change_base(5, 5)
    ' Tuesday'
    """
    return '{:0b}'.format(x, base)
```