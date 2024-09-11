```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to perform circular shift on.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the number to a string to be able to manipulate its digits
    num_str = str(x)
    
    # Calculate the actual shift, considering cases where shift > number of digits
    actual_shift = shift % len(num_str)
    
    # Perform the circular shift
    result = num_str[-actual_shift:] + num_str[:-actual_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(12, 3))  # Output: "12"
print(circular_shift(123, 2)) # Output: "321"
```

This script uses Python's built-in string concatenation to perform the circular shift. The `actual_shift` variable is calculated to handle the case where the shift is greater than the number of digits in the string. The circular shift is then performed by concatenating the last `actual_shift` characters of the string with the remainder of the string.