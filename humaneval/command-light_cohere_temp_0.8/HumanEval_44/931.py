```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the specified base.
    Returns the string representation of the number in the specified base.
    """

    base numbers are 10,
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 10)
    '99'
    >>> change_base(7, 5)
    TraceError: invalid literal for enum 'int': 'string'
    """
    return '{:0b}'.format(x, base)
```