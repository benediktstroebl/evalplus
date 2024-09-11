```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    num_str = str(x)
    
    # Calculate the actual shift, considering the case where shift > number of digits
    actual_shift = shift % len(num_str)
    
    # Split the string into two parts at the shift position
    first_part = num_str[-actual_shift:]
    second_part = num_str[:-actual_shift]
    
    # Combine the two parts in reverse order to get the shifted string
    shifted_str = first_part + second_part
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string and calculates the actual shift, considering the case where `shift > number of digits`. It then splits the string into two parts at the shift position, combines them in reverse order, and returns the result as a string. The script also includes test cases to demonstrate the function's behavior.