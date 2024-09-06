```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    return '{:b}'.format(x, base)
```