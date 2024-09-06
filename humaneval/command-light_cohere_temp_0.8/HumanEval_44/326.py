```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base b and return a string representation.
    >>> change_base(8, 3)  # Example of converting 8 to base 3
    '22'
    >>> change_base(5, 5) # Example of converting 5 to base 5
    '5'
    >>> change_base(123, 1) # Example of converting 123 to base 1
    '123'
    >>> change_base(123, 45) # Example of converting 123 to base 45
    '137'
    >>> change_base(123, 13) # Example of converting 123 to base 13
    '1323'
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return '0' + str(x)[2:] + '1'
    elif base == 1:
        return str(x)
    else:
        return '{:b}'.format(x, base)
```