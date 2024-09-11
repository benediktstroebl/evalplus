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
        str: The shifted digits as a string.
    """
    # Convert the integer to a string to easily access and manipulate individual digits
    x_str = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts at the shift point
    # The part to be moved to the end is sliced from the start to the shift point
    part_to_move = x_str[-effective_shift:]
    
    # The part that remains in its original position is sliced from the shift point to the end
    part_to_remain = x_str[:-effective_shift]
    
    # Combine the two parts to get the result
    result = part_to_move + part_to_remain
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses Python's built-in string slicing feature to split the input string into two parts at the shift point, moves the second part to the front, and combines them to produce the circular shift effect. The effective shift is calculated by taking the modulus of the shift with the length of the string to handle cases where shift is greater than the number of digits.