```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The shifted integer as a string
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert integer to string to easily manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    shift = shift % len(x_str)
    
    # Perform the circular shift
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    # Return the result
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses the modulus operator (`%`) to calculate the effective shift in case it's greater than the number of digits in the integer. It then performs the circular shift by concatenating the last `shift` characters of the string with the rest of the string (excluding the last `shift` characters). The result is returned as a string.