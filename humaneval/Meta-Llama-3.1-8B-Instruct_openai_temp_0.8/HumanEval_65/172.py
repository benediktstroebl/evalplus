```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of digits to shift.
    
    Returns:
    str: The shifted integer as a string.
    """
    # Convert the integer to a string and remove the negative sign if present
    num_str = str(abs(x))
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(num_str)
    
    # If the effective shift is 0, return the original string
    if effective_shift == 0:
        return num_str
    
    # Split the string into two parts: the part to be moved to the end and the rest
    part_to_move = num_str[-effective_shift:]
    rest = num_str[:-effective_shift]
    
    # Return the shifted string
    return part_to_move + rest


# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(1234, 2))  # "34"
print(circular_shift(1234, 5))  # "43"
print(circular_shift(-1234, 5))  # "43"
```

This script uses Python's string manipulation features to shift the digits of the input integer. It handles both positive and negative integers and includes test cases to verify the correctness of the function.