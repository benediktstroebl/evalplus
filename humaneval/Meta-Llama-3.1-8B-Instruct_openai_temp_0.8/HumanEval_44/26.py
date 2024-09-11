```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The new base for the number.

    Returns:
        str: The string representation of x in the new base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers")
    if x < 0 or base < 2 or base > 9:
        raise ValueError("x must be non-negative and base must be between 2 and 9")

    if x < base:
        return str(x)

    return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a recursive function `change_base` that converts a number `x` to a new base. It first checks if the input is valid, then uses integer division and modulus to recursively divide the number by the base and append the remainder to the result. The base case is when the number is less than the base, in which case it simply returns the string representation of the number.