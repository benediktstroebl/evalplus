```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits to the right.
        
    Returns:
        str: The result of the circular shift as a string.
    """
    
    # Convert the integer to a string to easily access its digits
    str_x = str(x)
    
    # Calculate the effective shift, handle cases where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    first_part = str_x[-effective_shift:]  # Get the last 'effective_shift' characters
    second_part = str_x[:-effective_shift]  # Get all but the last 'effective_shift' characters
    
    # Combine the two parts in reverse order to get the circularly shifted string
    result = first_part + second_part
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```