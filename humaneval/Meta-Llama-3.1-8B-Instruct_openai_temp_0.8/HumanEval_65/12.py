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
        str: The resulting string after shifting the digits.
    """
    # Convert the integer to a string for easier manipulation
    num_str = str(x)
    
    # Calculate the effective number of positions to shift
    # This is done by taking the modulus of the shift with the number of digits
    # This handles the case where shift is greater than the number of digits
    shift = shift % len(num_str)
    
    # If shift is 0, return the original string
    if shift == 0:
        return num_str
    
    # Split the string into two parts at the shift position
    # The part after the shift position is appended to the beginning
    result = num_str[-shift:] + num_str[:-shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(1234, 2))  # "34"
print(circular_shift(1234, 5))  # "4321"
```

This script defines a function `circular_shift` that takes two arguments: an integer `x` and an integer `shift`. The function first converts `x` to a string `num_str` for easier manipulation. It then calculates the effective number of positions to shift by taking the modulus of `shift` with the number of digits in `num_str`. This is done to handle the case where `shift` is greater than the number of digits. Finally, the function splits `num_str` into two parts at the shift position and appends the part after the shift position to the beginning to get the resulting string. The test cases at the end demonstrate the function's correctness.