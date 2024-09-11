Here's a Python function that implements the specified circular shift:
```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    # Convert the number to a string to easily access its digits
    str_x = str(x)
    
    # Calculate the actual shift, considering shifts greater than the number of digits
    actual_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the end and the rest
    # If the actual shift is greater than the number of digits, return the digits reversed
    if actual_shift > len(str_x):
        return str_x[::-1]
    
    # Split the string into two parts: the part to be shifted to the end and the rest
    part_to_shift = str_x[-actual_shift:]
    rest = str_x[:-actual_shift]
    
    # Combine the two parts to get the shifted string
    shifted_str = part_to_shift + rest
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Should print: 21
print(circular_shift(12, 2))  # Should print: 12
```
This script calculates the actual shift by taking the modulus of the shift with the number of digits in the input number. If the actual shift is greater than the number of digits, it returns the digits reversed. Otherwise, it splits the input string into two parts, shifts the first part to the end, and combines them to get the final result.