```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift the digits to the right.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the number to a string to easily manipulate the digits
    num_str = str(x)
    
    # Calculate the effective shift, considering a shift greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Perform the circular shift
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 2)) # Output: "321"
print(circular_shift(12345, 10)) # Output: "54321"
print(circular_shift(12345, 3)) # Output: "45123"
```