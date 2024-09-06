```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    return the string representation after conversion.
    base numbers other 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 10)
    '100000000000'
    """
    return format(x, '{}{}'.format(base, 'b')
```