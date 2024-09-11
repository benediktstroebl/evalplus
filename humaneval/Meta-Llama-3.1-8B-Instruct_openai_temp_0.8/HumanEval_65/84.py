```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits

    Returns:
        str: The result of the circular shift as a string
    """
    # Convert the integer to a string to easily manipulate its digits
    num_str = str(x)
    
    # Calculate the effective shift, considering the case where shift > len(num_str)
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts: the last 'effective_shift' characters and the rest
    # Then, swap their positions to achieve the circular shift
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Example usage:
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

In this script, we first convert the input integer to a string to easily manipulate its digits. We then calculate the effective shift, considering the case where shift > len(num_str), by taking the modulus of shift with the length of num_str. This ensures that we don't shift beyond the length of the string.

Next, we split the string into two parts: the last 'effective_shift' characters and the rest. We then swap their positions to achieve the circular shift. Finally, we return the shifted string.

This solution has a time complexity of O(n), where n is the number of digits in the input integer, and a space complexity of O(n) due to the string operations.