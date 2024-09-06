```python
def change_base(x: int, base: int):
    """
    Convert a number to a string representation in a specified base.
    Args:
        x: int, number to be converted
        base: int, base to use for conversion
    Returns:
        str: representation of x in base base
    """
    # Ensure base is less than 36
    if base > 36:
        base = 36
    result = ''
    while x:
        whole = x % base
        remainder = x // base
        result = chr(int(remainder + whole * 2)) + result
        x //= base
    return result
```