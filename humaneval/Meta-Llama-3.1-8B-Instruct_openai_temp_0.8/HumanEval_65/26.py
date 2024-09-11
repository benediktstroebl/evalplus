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
        str: The shifted integer as a string.
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the actual shift, in case shift > number of digits
    actual_shift = shift % len(num_str)
    
    # Split the string into two parts at the shift position
    first_part = num_str[-actual_shift:]
    second_part = num_str[:-actual_shift]
    
    # Concatenate the two parts in reverse order
    result = first_part + second_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift amount `shift` as input. It converts the integer to a string, calculates the actual shift, splits the string into two parts, and then concatenates them in reverse order. The result is returned as a string. The test cases demonstrate the function's behavior for different inputs.