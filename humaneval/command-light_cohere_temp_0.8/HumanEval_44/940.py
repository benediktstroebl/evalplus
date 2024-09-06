```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base
    >>> change_base(8, 3) == '22'
    >>> change_base(10, 3) == '333'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    # convert to string and then convert to desired base
    return str(x).format(x, format='{:b}'))
```