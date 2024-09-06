```python
def change_base(x: int, base: int):
    """
    Changes the base of a number to another base.
    Converts x to a corresponding string representation.
    Args:
        x: int, number to be converted
        base: int, desired base for the representation
    Returns:
        string representation of x, in the desired base
    """
    if base == 10:
        return str(x)
    elif base > 2 and base <= 36:
        return format(x, str(base))
    else:
        raise ValueError("Invalid base. Base must be between 2 and 36.")
```
This code defines a function `change_base` that converts a given number `x` to its string representation using the specified base. 
It first checks if the given base is valid, then, it uses the appropriate conversion method based on the base. 
Finally, it raises a ValueError if the base is not within the specified range.