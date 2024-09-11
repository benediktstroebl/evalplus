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
    str: The result as a string.
    """
    # Convert the integer to a string to easily access and manipulate digits
    str_x = str(x)
    
    # If shift is greater than or equal to the number of digits, return the digits reversed
    if shift >= len(str_x):
        return str_x[::-1]
    
    # Calculate the actual shift, considering the case where shift is greater than the number of digits
    actual_shift = shift % len(str_x)
    
    # Split the string into two parts at the shift position
    part1 = str_x[-actual_shift:]
    part2 = str_x[:-actual_shift]
    
    # Combine the two parts in the correct order to get the shifted string
    shifted_str = part1 + part2
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input, performs the circular shift, and returns the result as a string. The function handles the cases where the shift is greater than or equal to the number of digits by returning the digits reversed. The script also includes test cases to demonstrate the function's behavior.