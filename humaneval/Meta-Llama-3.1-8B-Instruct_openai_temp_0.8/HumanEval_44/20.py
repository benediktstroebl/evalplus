```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The string representation of x in base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9.")

    if x == 0:
        return '0'

    result = ""
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        
        # Prepend the remainder to the result string
        result = str(remainder) + result
        
        # Update x to be the quotient of x divided by base
        x //= base

    return result

# Example usage
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script includes type checking to ensure that `x` and `base` are integers, and that `base` is between 2 and 9. It also handles the edge case where `x` is 0. The function uses a while loop to repeatedly divide `x` by `base` and prepend the remainder to the result string until `x` is 0. The result string is then returned.