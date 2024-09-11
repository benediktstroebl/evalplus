```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily extract and manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account the length of the string
    # This is done by finding the remainder of the shift divided by the length of the string
    # This is because a shift of n places is the same as a shift of (n % len(str_x)) places
    effective_shift = shift % len(str_x)
    
    # If the effective shift is 0, return the original string
    if effective_shift == 0:
        return str_x
    
    # Split the string into two parts: the part to be shifted to the end and the part to be shifted to the front
    # The part to be shifted to the end is the substring from the index of the effective shift to the end
    end_part = str_x[-effective_shift:]
    
    # The part to be shifted to the front is the substring from the start to the index of the effective shift
    front_part = str_x[:-effective_shift]
    
    # Return the result by concatenating the two parts in the correct order
    return end_part + front_part

# Example usage:
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift as a string. The function first converts the integer to a string, calculates the effective shift, and then splits the string into two parts: the part to be shifted to the end and the part to be shifted to the front. Finally, it returns the result by concatenating the two parts in the correct order.