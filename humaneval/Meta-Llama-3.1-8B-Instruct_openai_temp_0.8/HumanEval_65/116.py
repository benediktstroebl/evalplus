```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The string representation of the shifted integer.
    """
    
    # Convert the integer to a string to easily access and manipulate its digits
    num_str = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into a list of characters (digits)
    digits = list(num_str)
    
    # Shift the digits to the right
    digits = digits[-effective_shift:] + digits[:-effective_shift]
    
    # Join the digits back into a string
    shifted_str = ''.join(digits)
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines the `circular_shift` function that takes an integer `x` and a shift value `shift`. It first converts the integer to a string, calculates the effective shift, splits the string into a list of digits, shifts the digits to the right, and then joins the digits back into a string. It then tests the function with the provided example inputs.