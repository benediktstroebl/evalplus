```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Args:
        x: int, The number to be converted
        base: int, The base to convert to
    Returns: string representation of x in the specified base
    """
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    # math.is is used out that both numbers and base are positive integers
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.
    # Convert the _ to string representation using the corresponding number format
    return format(x, '{:b}' if base == 10 else '{b}'.format(x, base))

# Test the function
x = 8
try:
    y = change_base(x, 10)
    print(y)
except ValueError as e:
    print(f"Error: {e}")

# Test valid base numbers
print(change_base(7, 2))
print(change_base(12, 8))
print(change_base(23, 5))
``` 
This code defines a function change_base that takes an integer x and a base b as input, and returns the string representation of x in the specified base. The base numbers are in the range of 2 to 36, and the function raises an error if an invalid base number is provided. It also handles negative numbers, raising a ValueError. This ensures that only valid inputs are processed, and the function provides a clear error message for invalid inputs.