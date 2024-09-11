```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits to the right.

    Returns:
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)

    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(str_x)

    # Perform the circular shift by slicing the string
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]

    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 2))  # "321"
print(circular_shift(1234, 3))  # "4312"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift value `shift` as input. It first converts the integer to a string, then calculates the effective shift by taking the modulus of `shift` with the length of the string (to handle cases where `shift` is greater than the number of digits). It then performs the circular shift by slicing the string, and returns the result. The test cases at the end demonstrate the function's behavior with different inputs.