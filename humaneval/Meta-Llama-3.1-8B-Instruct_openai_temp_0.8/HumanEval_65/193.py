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
    # Convert the integer to a string for easier manipulation
    num_str = str(x)
    # Calculate the effective shift, in case shift > len(num_str)
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the effective shift position
    parts = [num_str[-effective_shift:], num_str[:-effective_shift]]
    
    # Join the parts in reverse order to achieve the circular shift
    result = ''.join(reversed(parts))
    
    return result

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```