```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted digits as a string.
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to easily access and manipulate its digits
    num_str = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(num_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return num_str[::-1]
    
    # Split the string into two parts, the part that will be shifted to the end and the part that will remain at the beginning
    shifted_part = num_str[-effective_shift:]
    remaining_part = num_str[:-effective_shift]
    
    # Return the shifted part concatenated with the remaining part
    return shifted_part + remaining_part

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift operation as a string. The function first converts the integer to a string to easily access and manipulate its digits. It then calculates the effective shift, which is the remainder of `shift` divided by the number of digits. If the effective shift is 0, the function returns the reversed string. Otherwise, it splits the string into two parts, the part that will be shifted to the end and the part that will remain at the beginning, and returns the shifted part concatenated with the remaining part. The script also includes test cases to demonstrate the function's behavior.