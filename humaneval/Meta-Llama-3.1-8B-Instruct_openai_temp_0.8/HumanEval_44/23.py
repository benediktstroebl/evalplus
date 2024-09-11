```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The input number to be converted.
    base (int): The target base.

    Returns:
    str: String representation of the number in the target base.

    """
    # Check if the base is valid
    if base < 2 or base > 10:
        raise ValueError("Invalid base. Base should be between 2 and 10.")

    # Handle the case when x is 0
    if x == 0:
        return '0'

    digits = []
    while x:
        # Get the remainder of x divided by base
        remainder = x % base
        # Append the remainder to the list of digits
        digits.append(str(remainder))
        # Update x to be the quotient of x divided by base
        x //= base

    # Reverse the list of digits and join them into a string
    return ''.join(reversed(digits))

# Test cases
print(change_base(8, 3))  # Should print '22'
print(change_base(8, 2))  # Should print '1000'
print(change_base(7, 2))  # Should print '111'
```

This script defines a function `change_base` that converts an integer `x` to a string representation in a target base. The function first checks if the base is valid (between 2 and 10). It then handles the special case when `x` is 0, returning `'0'` immediately. 

For non-zero `x`, the function repeatedly calculates the remainder of `x` divided by `base`, appends this remainder to the list of digits, and updates `x` to be the quotient of `x` divided by `base`. This process continues until `x` becomes 0. The function then reverses the list of digits and joins them into a string, which is the final result. 

The provided test cases demonstrate the correctness of the function.