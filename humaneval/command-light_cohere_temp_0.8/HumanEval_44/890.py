```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Parameters:
        x: int (number to be base converted)
        base: int (target base)
    Returns: string representation of the converted number
    """
    if base == 10:
        return str(x)
    elif 6 <= base <= 36:
        return '{:0{}b}'.format(x, base)
    else:
        raise ValueError("Invalid base number. Not a 10 or suchows a base, 6 <= base <= 36")
```