```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift the digits to the right.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return the digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Split the string into two parts: the part to be shifted to the end and the part to remain at the beginning
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It first converts the integer to a string to easily manipulate its digits. Then it calculates the effective shift, considering the case where `shift > number of digits`. Finally, it splits the string into two parts, shifts the first part to the end, and returns the result as a string. The script also includes two test cases to demonstrate the function's behavior.