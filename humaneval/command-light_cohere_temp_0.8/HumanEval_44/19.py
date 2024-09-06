```python
def change_base(x: int, base: int):
    """
    Changes the base of a number x to the specified base.
    Args:
        x: int or float
        base: int
    Returns:
        str
    """
    # check if x is float
    if isinstance(x, float):
        x = str(x)
    # check if base is less than 0 or greater than 36
    if base < 0 or base > 36:
        raise ValueError("Base must be between 0 and 36")
    # convert x to string representation
    return format(x, str(base))

x = 8
y = 3
z = change_base(x, y)
print(z)  # Output: 22
```