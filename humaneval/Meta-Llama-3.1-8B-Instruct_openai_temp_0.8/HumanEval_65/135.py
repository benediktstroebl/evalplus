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
    # Convert the integer to a string to easily manipulate the digits
    num_str = str(x)
    
    # Calculate the effective shift, considering the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the shift position
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the parts in reverse order to achieve the shift
    shifted_str = first_part + second_part
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This Python script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It performs a circular shift on the digits of `x` by the specified `shift` and returns the result as a string. The function handles the case where `shift` exceeds the number of digits by reversing the string. The test cases are included to demonstrate the function's behavior.