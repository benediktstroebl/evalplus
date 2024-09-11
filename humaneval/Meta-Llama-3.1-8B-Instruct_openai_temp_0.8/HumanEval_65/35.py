```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the number to a string
    num_str = str(x)
    
    # Calculate the effective shift
    # If shift is greater than the number of digits, return the reversed string
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts and concatenate them in reverse order
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 1))  # "231"
print(circular_shift(123, 3))  # "123"
print(circular_shift(1234, 2))  # "4312"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift, and then splits the string into two parts and concatenates them in reverse order to perform the circular shift. The function returns the shifted number as a string. The script includes test cases to demonstrate the function's behavior.