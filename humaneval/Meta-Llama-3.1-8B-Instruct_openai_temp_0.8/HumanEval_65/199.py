```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted integer as a string.
    """
    
    # Convert the integer to a string to operate on digits
    str_x = str(x)
    
    # Calculate the actual shift, considering cases where shift > number of digits
    actual_shift = shift % len(str_x)
    
    # Split the string into two parts, considering the actual shift
    shifted_str = str_x[-actual_shift:] + str_x[:-actual_shift]
    
    # Return the result
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

In this script, the `circular_shift` function first converts the input integer `x` to a string. It then calculates the actual shift, which is the remainder of the shift divided by the length of the string. This is because shifting by a multiple of the number of digits is the same as not shifting at all.

Next, the function splits the string into two parts, considering the actual shift. The part to be moved to the beginning of the string starts from the end of the original string and has a length equal to the actual shift.

Finally, the function returns the shifted string by concatenating the two parts.

The script includes test cases to demonstrate the function's behavior for different inputs.