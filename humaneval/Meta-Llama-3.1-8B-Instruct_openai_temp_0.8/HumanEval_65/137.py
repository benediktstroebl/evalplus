```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of digits to shift.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    # The second part will be appended to the beginning of the result
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift as a string. The function uses the modulo operator (`%`) to calculate the effective shift, in case `shift` is greater than the number of digits in `x`. The function then splits the string representation of `x` into two parts at the effective shift position, appends the second part to the beginning of the result, and returns the result. The script includes test cases to demonstrate the function's behavior.