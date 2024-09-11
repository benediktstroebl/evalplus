```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, which is the shift modulo the number of digits
    # This handles the case where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the beginning, and the rest
    # The part to be shifted to the beginning is the last effective_shift digits
    # The rest is the remaining part
    str_x_beginning = str_x[-effective_shift:]
    str_x_rest = str_x[:-effective_shift]
    
    # Return the shifted string by concatenating the two parts
    return str_x_beginning + str_x_rest

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```
This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input. It returns the shifted integer as a string. The function works by first converting the integer to a string, then calculating the effective shift by taking the modulus of the shift with the number of digits. It then splits the string into two parts, shifts the second part to the beginning, and concatenates the two parts to get the final result.