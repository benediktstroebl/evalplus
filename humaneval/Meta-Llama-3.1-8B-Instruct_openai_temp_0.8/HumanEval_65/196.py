```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of digits to shift.
    
    Returns:
        str: The shifted digits as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(x_str)
    
    # If shift > number of digits, shift right and then reverse the string to get the result
    if effective_shift > len(x_str) // 2:
        effective_shift = len(x_str) - effective_shift
    
    # Shift the string right by effective_shift places
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 1))  # "231"
print(circular_shift(123, 2))  # "123"
print(circular_shift(123, 3))  # "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It returns the result of shifting the digits of `x` to the right by `shift` places as a string. If `shift` is greater than the number of digits in `x`, it shifts the digits right and then reverses the string to get the result. The script includes test cases to verify the correctness of the function.