```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
    first.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 5) # invalid base raises ValueError
    ValueError: cannot represent number: base 5 is not a matching base
    >>> change_base('12', 2) # invalid input raises ValueError
    ValueError: cannot represent number: '12' is not an integer
    """
    if base not in [2, 'o', 'e', 'x', 'b', 'B']:
        raise ValueError("base must be 2, 'o', 'e', 'x', 'b', 'B')
    return format(x, base)
```