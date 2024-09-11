### Circular Shift Script
```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to easily access and modify its digits
    str_x = str(x)
    
    # Calculate the effective shift by taking the modulus of the shift with the number of digits
    # This handles the case where shift > number of digits
    shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the end, and the part to remain at the start
    # The part to be shifted to the end starts from the shift position to the end of the string
    end_part = str_x[-shift:]
    
    # The part to remain at the start starts from the beginning of the string to the shift position
    start_part = str_x[:-shift]
    
    # Combine the two parts to form the result
    result = end_part + start_part
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input. It converts the integer to a string, calculates the effective shift by taking the modulus of the shift with the number of digits, splits the string into two parts, and combines them to form the result. The function then returns the result as a string. The script also includes test cases to demonstrate the function's correctness.