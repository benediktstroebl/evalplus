```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    # Ensuring that the numbers can be converted to a string
    x = str(x)
    return format(x, '{}'.format, base)
```