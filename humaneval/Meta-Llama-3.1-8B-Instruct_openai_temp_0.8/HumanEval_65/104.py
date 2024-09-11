```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift.

    Returns:
        str: The result as a string.
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the actual shift, considering cases where shift > number of digits
    actual_shift = shift % len(num_str)
    
    # Split the string into two parts and shift the second part to the left
    shifted_str = num_str[-actual_shift:] + num_str[:-actual_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It first converts the integer to a string, then calculates the actual shift value by taking the modulus of `shift` with the length of the string. This is to handle cases where `shift` is greater than the number of digits in the integer. The string is then split into two parts and the second part is shifted to the left by the actual shift value. The resulting string is then returned. The script also includes test cases to demonstrate the function's behavior.