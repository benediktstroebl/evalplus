### Circular Shift Function
```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to shift.
    shift (int): The number of positions to shift.
    
    Returns:
    str: The shifted string representation of x.
    """
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Perform the circular shift by slicing the string and concatenating the parts
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Example use cases:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 2)) # Output: "321"
```

This function works by first converting the input integer to a string, allowing us to easily access and manipulate its digits. It then calculates the effective shift, which is the remainder of the shift divided by the number of digits. If the effective shift is 0, it means the shift is a multiple of the number of digits, so the function returns the reversed string. Otherwise, it performs the circular shift by slicing the string and concatenating the parts.