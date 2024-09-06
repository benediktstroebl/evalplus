```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    if base < 2 or base > 36:
        raise ValueError("Base number should be between 2 and 36")

    return format(x, f"{base}".format)
```  The function changes the base of a number to another base and returns the formatted string.