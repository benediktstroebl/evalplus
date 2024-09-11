```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to perform the circular shift on.
        shift (int): The number of positions to shift the digits to the right.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(str_x)
    # Shift the digits to the right using string slicing
    shifted_str_x = str_x[-effective_shift:] + str_x[:-effective_shift]
    # Return the result as a string
    return shifted_str_x

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input. It first converts the integer to a string to easily manipulate the digits. It then calculates the effective shift amount by taking the modulus of the shift amount with the length of the string (to handle cases where the shift amount is greater than the number of digits). Finally, it shifts the digits to the right using string slicing and returns the result as a string. The script includes test cases to demonstrate the function's behavior.