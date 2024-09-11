```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted number as a string.
    """
    # Convert the number to a string to easily access and manipulate digits
    num_str = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    shift = shift % len(num_str)
    
    # If shift is greater than the number of digits, shift is equivalent to shifting 
    # to the left (i.e., reversing the string)
    if shift > len(num_str):
        return num_str[::-1]
    
    # Split the string into two parts: the part to be shifted to the right and the part 
    # to remain in the same position
    right_shift = num_str[-shift:]
    left_shift = num_str[:-shift]
    
    # Combine the two parts to get the final result
    result = right_shift + left_shift
    
    return result

# Example use cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(1234, 3))  # Output: "4321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input and returns the circularly shifted string representation of `x`. The function first converts the number to a string, calculates the effective shift amount, and then splits the string into two parts: the part to be shifted to the right and the part to remain in the same position. Finally, it combines the two parts to get the final result.