```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.

    Args:
    x (int): The number to be converted.
    base (int): The base to convert to. Must be less than 10.

    Returns:
    str: A string representation of the number in the specified base.

    Raises:
    ValueError: If the base is not less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")

    if x == 0:
        return '0'

    result = ''
    while x > 0:
        # Calculate the remainder of x divided by base
        remainder = x % base

        # If the remainder is greater than 9, convert it to a letter
        if remainder > 9:
            result = chr(ord('A') + remainder - 10) + result
        else:
            result = str(remainder) + result

        # Update x to be the quotient of x divided by base
        x = x // base

    return result

# Test the function
print(change_base(8, 3))  # Outputs: '22'
print(change_base(8, 2))  # Outputs: '1000'
print(change_base(7, 2))  # Outputs: '111'
```

This script defines the `change_base` function, which takes an integer `x` and a base `base` as input, and returns a string representation of `x` in the specified base. The function handles bases less than 10 by using letters to represent numbers greater than 9 (A=10, B=11, etc.). It also checks if the base is valid and raises a `ValueError` if it's not between 2 and 9. The script includes test cases to demonstrate the function's usage.