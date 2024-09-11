```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits

    Returns:
        str: The result as a string
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, considering the case where shift > len(str_x)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    # and then combine them in reverse order
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value as input, performs the circular shift operation, and returns the result as a string. The script also includes test cases to verify the correctness of the function.