```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number to the specified base.
    Args:
        x: int, the number to be converted
        base: int, the base to convert to
    Returns:
        str: string representation of the number with the new base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.
    return format(x(x), base).
    return format(x, base)
``` 
The `change_base` function takes two arguments: `x` and `base`. It then checks the base of `base` to ensure it's valid, and uses the `format` function to convert the number to the specified base.