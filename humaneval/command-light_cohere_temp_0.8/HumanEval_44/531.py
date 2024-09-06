```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    Convert x from string representation using the base numbers.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    return format(x, base)
```