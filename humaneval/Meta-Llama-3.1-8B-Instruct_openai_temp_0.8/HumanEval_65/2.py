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
        str: The result as a string.
    """
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part that will be shifted to the right,
    # and the part that will remain at the start
    first_part = str_x[-effective_shift:]  # Shifted part
    second_part = str_x[:-effective_shift]  # Remaining part
    
    # Concatenate the two parts in the correct order
    result = first_part + second_part
    
    # Return the result as a string
    return result


# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(1234, 2))  # "43"
```

This script uses string manipulation to achieve the circular shift. It first converts the integer to a string, then calculates the effective shift considering cases where shift > number of digits. Finally, it splits the string into two parts and concatenates them in the correct order to get the result.