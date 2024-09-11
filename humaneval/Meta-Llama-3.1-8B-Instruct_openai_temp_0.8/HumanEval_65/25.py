```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted integer as a string.
    """
    
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts at the effective shift position
    first_part = x_str[-effective_shift:]
    second_part = x_str[:-effective_shift]
    
    # Combine the two parts in reverse order to achieve the circular shift
    result = first_part + second_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```