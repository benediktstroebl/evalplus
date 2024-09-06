```python
def change_base(x: int, base: int):
    """
    Convert a number to a string representation using specified base.
    Args:
        x: int, number to be converted
        base: int, base for string representation
    Returns:
        str: converted number as a string
    """
    if x < 0 or base < 2 or base > 36:
        raise ValueError("Invalid base for conversion.")
    if base == 10:
        return str(x)
    elif base == 2:
        return str(x, base=16)
    elif base == 16:
        return str(x, base=16)
    elif base == 8:
        return str(x, base=2).
    else:
        return str(x, base=base)
```