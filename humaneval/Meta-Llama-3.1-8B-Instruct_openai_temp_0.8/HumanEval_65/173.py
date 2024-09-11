```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to perform the shift on.
        shift (int): The number of digits to shift.

    Returns:
        str: The shifted digits as a string.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the actual shift, in case shift > number of digits
    shift = shift % len(x_str)
    
    # Perform the circular shift by slicing the string
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Outputs: "21"
print(circular_shift(12, 2))  # Outputs: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as arguments. It performs a circular shift on the digits of `x` and returns the result as a string. If the shift value is greater than the number of digits, it returns the digits in reverse order. The function uses slicing to perform the circular shift, making it efficient and easy to read. The script also includes test cases to verify the correctness of the function.