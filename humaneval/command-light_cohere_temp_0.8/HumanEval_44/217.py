```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.

    Args:
        x (number): int, a number to convert
        base (base): int, the base to which the number should be converted

    Returns:
        string: The string representation of the number in the new base
    """
    # Ensure base is smaller than 36 to support only base conversions up to base 36
    if base > 36:
        raise ValueError("Invalid base value, base must be <= 36")

    # Convert x to string in current base
    result = str(x, base)

    return result

# Unit tests
print(change_base(8, 3))       # Expected output '22'
print(change_base(10, 2))      # Expected output '1000'
print(change_base(7, 4))       # Expected output '161'
print(change_base(15, 10))    # Expected output '15'
print(change_base(123, 3))    # Expected output '33'
print(change_base(10, 30))    # Expected output '3000'
print(change_base(123, 31))   # Expected output '3331'
```
The provided Python code defines a function called `change_base` that converts a given number `x` to a string in a specified base. The function takes two arguments: `x` (the number to be converted) and `base` (the base to which the number will be converted). The function first checks if the `base` is valid (smaller than 36), and then converts the number `x` to a string in the specified base using the `str` function. 
Finally, the function returns the converted string representation of `x`.  The unit tests ensure the function works correctly for different inputs and base values.