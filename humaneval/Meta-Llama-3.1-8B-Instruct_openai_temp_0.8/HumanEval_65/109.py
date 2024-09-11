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
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    num_str = str(x)
    
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the effective shift position
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the two parts in reverse order to get the shifted string
    shifted_str = first_part + second_part
    
    # If the shift is greater than the number of digits, return the digits reversed
    if shift > len(num_str):
        return num_str[::-1]
    
    # Otherwise, return the shifted string
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
```