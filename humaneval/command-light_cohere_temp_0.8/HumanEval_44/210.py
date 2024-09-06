```python
def change_base(x: int, base: int):
    """
    Change the base numerical number x to base.
    return string representation after conversion.
    base numbers are
    support base 2 and 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 10)
    '1123'
    >>> change_base(123, 2)
    '22'
    >>> change_base(123, 5) #Invalid input
    '55555'
    >>> change_base(123, 'abc') #Invalid base
    'abc'
    """
    if base not in [2, 10]:
        raise ValueError("Base must be either 2 or 10")
    return '{:0{}d}'.format(x, base)
```