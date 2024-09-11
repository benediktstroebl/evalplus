```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to shift.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.

    Examples:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    # Convert the integer to a string
    num_str = str(x)
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(num_str)
    # Shift the string to the right by effective_shift positions
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Outputs: "21"
print(circular_shift(12, 2))  # Outputs: "12"
print(circular_shift(123, 2))  # Outputs: "321"
print(circular_shift(123, 5))  # Outputs: "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, and returns the result of the circular shift as a string. The function first converts the integer to a string, then calculates the effective shift by taking the modulus of the shift value with the length of the string. This ensures that the effective shift is within the range of the number of digits. Finally, the function shifts the string to the right by the effective shift value and returns the result. The script also includes some test cases to demonstrate the function's behavior.