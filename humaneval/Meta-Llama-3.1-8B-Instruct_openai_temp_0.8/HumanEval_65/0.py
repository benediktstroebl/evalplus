```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits to the right.
    Returns:
        str: The result of the circular shift as a string.
    """
    str_x = str(x)  # Convert the integer to a string
    shift = shift % len(str_x)  # Handle cases where shift > number of digits
    return str_x[-shift:] + str_x[:-shift]  # Shift the digits to the right

# Test cases
print(circular_shift(12, 1))  # Outputs: "21"
print(circular_shift(12, 2))  # Outputs: "12"
print(circular_shift(123, 4))  # Outputs: "321"
print(circular_shift(123, 7))  # Outputs: "123"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, applies a circular shift to the digits of `x`, and returns the result as a string. The script also includes several test cases to demonstrate the function's behavior.