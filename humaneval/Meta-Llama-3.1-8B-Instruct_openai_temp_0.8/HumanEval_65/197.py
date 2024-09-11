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
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the actual shift, taking into account if shift > number of digits
    actual_shift = shift % len(str_x)
    
    # Split the string into two parts at the shift point
    first_part = str_x[-actual_shift:]
    second_part = str_x[:-actual_shift]
    
    # Combine the two parts to get the result
    result = first_part + second_part
    
    return result

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

In this script, we first convert the input integer to a string to easily manipulate its digits. Then we calculate the actual shift by taking the modulus of the shift with the number of digits. This handles the case where shift is greater than the number of digits. We then split the string into two parts at the shift point, combine them, and return the result.