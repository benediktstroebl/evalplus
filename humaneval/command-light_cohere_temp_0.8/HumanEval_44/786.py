Here's a Python script that contains a self-contained function to change the numerical base of a number:

```python
def change_base(x, base):
    """Changes the base of a number x to base b.
    : Does not convert bases <0, < 2, or > 36.
    Args:
        x: int or string, base: int
    Returns:
        string representation of the number with the new base
    """
    if x == "" or base == 0 or base < 2 or base > 36:
        raise ValueError("Base should be a positive integer greater than 0 and less than 37")

    # Convert string to integer
    x = int(x)

    if base < 2:  # special case for base less than 2
        return str(x * base)

    return format(x, f"{base:b}",1000)  # use built-in format with base and padding with 1000
```

This script defines a function `change_base` which converts a number to a new base. The function performs a validation on the base argument to ensure it is valid and then uses the `format` function to convert the number to the new base. The function supports both basic cases for converting a string to an integer as well.