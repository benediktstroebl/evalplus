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
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    str_x = str(x)
    
    # Calculate the actual shift, taking into account the length of the string
    # If shift is greater than the length of the string, it's equivalent to
    # shifting by the remainder of shift divided by the length of the string
    actual_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the right and
    # the part to be shifted to the left
    right_part = str_x[-actual_shift:]
    left_part = str_x[:-actual_shift]
    
    # Combine the two parts in the correct order
    result = right_part + left_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift as a string. It uses string manipulation to achieve the circular shift. The test cases at the end demonstrate the function's correctness.