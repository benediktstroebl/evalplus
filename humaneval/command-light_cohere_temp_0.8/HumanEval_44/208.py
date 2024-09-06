```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base b.
    >>> change_base(8, 3)  # returns '22'
    >>> change_base(8, 2)  # returns '1000'
    >>> change_base(7, 2)  # returns '111'
    """
    if base == 10:
        return str(x)
    return "{:.2f}".format(x, base)
```