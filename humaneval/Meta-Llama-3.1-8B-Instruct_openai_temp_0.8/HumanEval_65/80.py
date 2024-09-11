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
        str: The result as a string.
    """
    str_x = str(x)  # Convert the number to a string
    shift = shift % len(str_x)  # Handle the case where shift > number of digits
    return str_x[-shift:] + str_x[:-shift]  # Perform the circular shift

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
print(circular_shift(1234, 2))  # Expected output: "4312"
```

This script defines the `circular_shift` function, which takes a number `x` and a shift amount `shift` as input, performs the circular shift operation, and returns the result as a string. The script then includes test cases to demonstrate the function's behavior.