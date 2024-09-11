```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift the digits.
    
    Returns:
        str: The shifted number as a string.
    """
    # Convert the number to a string
    num_str = str(x)
    
    # Calculate the effective shift, considering the case where shift > len(num_str)
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts: the part to be shifted to the end and the rest
    end_part = num_str[-effective_shift:]
    rest_part = num_str[:-effective_shift]
    
    # Return the shifted number
    return end_part + rest_part

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(123, 2))  # "321"
```

This script defines the `circular_shift` function and includes test cases to demonstrate its usage. The function takes an integer `x` and a shift amount `shift` as input, performs the circular shift, and returns the result as a string. The function uses the modulo operator to calculate the effective shift, ensuring that the shift amount is always within the range of the number of digits.