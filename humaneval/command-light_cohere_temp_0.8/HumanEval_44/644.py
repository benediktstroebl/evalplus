```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number to base 'base'.
    Returns the string representation of the number.
    """
    following the base numbers are 10 or implementation specific
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    if x < 0:
        raise ValueError("Input number cannot be negative.")
    if base == 10:
        return str(x)
    if base > 10:
        return f"{x:>{base}'".format(x)
    else:
        return str(int(x) * int((1 << base) - 1))
```