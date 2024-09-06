```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    """
    number in scientific notation and convert it into a string
    representation.

    Args:
    x: int, number to be converted
    base: int, conversion base

    Returns:
    str, string representation of x in the specified base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Use numbers between 2 2 and 36")
    # Ensure x is in scientific notation
    x = str(x) + 'e' + '+' + str(x[-1])
    return f'{x:>{base}'  # use f-string formatting for string representation
```
The function takes an integer `x` and an integer `base` as input and returns the string representation of `x` in the specified base.  It ensures that the base is valid, between 2 and 36, and then converts `x` into scientific notation and appends an 'e' to get rid of the decimal point.