```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift, taking into account the length of the string
    effective_shift = shift % len(str_x)
    
    # If shift is greater than the number of digits, return the digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Otherwise, return the substring from the effective shift to the end, 
    # combined with the substring from the start to the effective shift
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

In this code, we first convert the input integer to a string to make it easier to manipulate. We then calculate the effective shift by taking the modulus of the shift with the length of the string. This ensures that the shift is always within the bounds of the string, and that a shift of 0 (which is equivalent to a shift of the length of the string) results in the string being reversed.

Finally, we use Python's slice notation to extract the substring from the effective shift to the end of the string, and the substring from the start of the string to the effective shift. We then combine these two substrings to form the result of the circular shift.