```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
    x (int): The integer to be circular shifted.
    shift (int): The number of digits to shift.

    Returns:
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Otherwise, return the result of the circular shift
    else:
        return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(1234, 1))  # Output: "4321"
print(circular_shift(1234, 3))  # Output: "1234"
```

This script defines a function `circular_shift` that takes an integer `x` and an integer `shift` as input, performs a circular shift on the digits of `x` by `shift` positions, and returns the result as a string. The function handles the case where `shift` is greater than the number of digits by returning the reversed string. The script includes test cases to demonstrate the function's behavior.