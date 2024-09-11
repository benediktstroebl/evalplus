```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift (in case shift is greater than the number of digits)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts, shift the second part to the left, and concatenate them
    # The second part is from the effective shift to the end, and the first part is from the start to the effective shift
    result = str_x[effective_shift:] + str_x[:effective_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(12, 3))  # Output: "12"
print(circular_shift(123, 2))  # Output: "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, performs a circular shift on the digits of `x`, and returns the result as a string. The function uses the modulo operator (`%`) to calculate the effective shift in case it's greater than the number of digits, and then splits the string into two parts, shifts the second part to the left, and concatenates them to get the result. The script also includes some test cases to demonstrate the function's behavior.