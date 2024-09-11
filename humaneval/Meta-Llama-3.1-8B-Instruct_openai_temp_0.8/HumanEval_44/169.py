```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target base.

    Returns:
        str: String representation of x in base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Inputs must be integers")
    if x < 0 or base < 2 or base > 10:
        raise ValueError("x must be non-negative and base must be between 2 and 10")

    digits = "0123456789"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a recursive function `change_base` to convert a number `x` from base 10 to a specified base. The function uses string concatenation to build the result and handles cases where the input number is less than the target base by directly returning the corresponding digit string. The test cases at the end demonstrate the function's behavior.