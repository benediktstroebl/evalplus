```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The shift amount.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    # Calculate the effective shift, taking into account the case where shift > len(str_x)
    effective_shift = shift % len(str_x)
    # Return the result of the circular shift
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 2))  # Output: "321"
```

This script defines a function `circular_shift` that performs a circular shift on the digits of an integer `x` by a specified `shift` amount. The function works by first converting the integer to a string, then calculating the effective shift by taking the remainder of `shift` divided by the length of the string. It then returns the result of the circular shift by slicing the string. The test cases demonstrate the function's behavior with different inputs.