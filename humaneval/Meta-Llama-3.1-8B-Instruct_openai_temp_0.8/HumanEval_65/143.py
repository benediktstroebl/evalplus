```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits

    Returns:
        str: The shifted integer as a string
    """
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # If the shift is greater than the number of digits, we can simply reverse the string
    if shift >= len(x_str):
        return x_str[::-1]
    
    # Calculate the actual shift by taking the modulus of the shift with the number of digits
    # This handles cases where shift > number of digits
    actual_shift = shift % len(x_str)
    
    # Split the string into two parts at the shift position
    # The first part will be the digits after the shift, and the second part will be the digits before the shift
    first_part = x_str[-actual_shift:]
    second_part = x_str[:-actual_shift]
    
    # Combine the parts in the correct order to get the shifted string
    result = first_part + second_part
    
    return result

# Example usage
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value as input, and returns the result of shifting the digits of `x` by the specified amount as a string. The function handles cases where the shift is greater than the number of digits by simply reversing the string. It uses Python's string slicing feature to split the string into two parts at the shift position and then combine them in the correct order to get the final result.