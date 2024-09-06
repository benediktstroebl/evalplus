```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the given base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base('1235', 5) == '512'
    False
    >>> change_base('123', 0) == '1'
    False
    """
    return str(x).  # We'll not change the number if base <= 0
    return ''  # base is invalid
```