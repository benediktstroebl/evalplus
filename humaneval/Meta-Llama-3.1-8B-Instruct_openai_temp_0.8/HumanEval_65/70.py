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
    # Convert the integer to a string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the end, and the part to keep at the beginning
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    
    # Combine the two parts in the correct order and return the result
    return first_part + second_part


# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses Python's built-in string manipulation functions to solve the problem. It converts the input integer to a string, calculates the effective shift, and then combines the two parts of the string in the correct order to produce the result.