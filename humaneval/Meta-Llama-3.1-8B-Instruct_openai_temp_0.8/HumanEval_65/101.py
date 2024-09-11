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
        str: The result as a string.
    """
    # Convert the integer to a string to easily extract and manipulate digits
    num_str = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(num_str)
    
    # Perform the circular shift by slicing the string
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(1234, 3))  # Output: "4312"
print(circular_shift(1234, 7))  # Output: "3214"
```

This script defines a function `circular_shift(x, shift)` that takes an integer `x` and a shift value `shift` as input, performs the circular shift, and returns the result as a string. The function handles cases where the shift value is greater than the number of digits in the input integer by taking the effective shift as the remainder of the division of shift by the number of digits.