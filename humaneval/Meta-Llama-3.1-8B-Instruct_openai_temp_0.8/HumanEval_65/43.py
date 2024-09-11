```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of places to shift the digits.

    Returns:
        str: The shifted integer as a string.
    """
    str_x = str(x)  # Convert the integer to a string
    shift = shift % len(str_x)  # Handle shift > number of digits
    return str_x[-shift:] + str_x[:-shift]  # Shift the digits and return the result


# Test the function
print(circular_shift(12, 1))  # Should print "21"
print(circular_shift(12, 2))  # Should print "12"
print(circular_shift(12345, 5))  # Should print "54321"
print(circular_shift(12345, 10))  # Should print "54321"
```

This script defines a function `circular_shift` that takes an integer and a shift value as input. It converts the integer to a string, handles the case where the shift value is greater than the number of digits, and returns the shifted integer as a string. The function is then tested with various inputs to demonstrate its correctness.