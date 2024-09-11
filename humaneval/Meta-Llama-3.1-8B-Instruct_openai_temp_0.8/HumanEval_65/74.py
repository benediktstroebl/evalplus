```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to be shifted
    shift (int): The number of positions to shift the digits of x to the right
    
    Returns:
    str: The shifted number as a string
    """
    
    # Convert the integer to a string to easily manipulate its digits
    num_str = str(x)
    
    # Calculate the effective shift, in case shift is greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts: the part to be moved to the end, and the part to stay at the beginning
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the two parts in the correct order to get the shifted number
    shifted_num = first_part + second_part
    
    return shifted_num

# Test the function
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of shifting the digits of `x` to the right by `shift` positions. The function first converts the integer to a string, calculates the effective shift in case it's greater than the number of digits, splits the string into two parts, and combines them in the correct order to get the shifted number. The function is then tested with the provided example inputs.