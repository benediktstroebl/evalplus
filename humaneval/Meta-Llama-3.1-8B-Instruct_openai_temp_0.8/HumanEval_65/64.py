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
    num_str = str(x)
    
    # Calculate the effective shift
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts
    # The part to be shifted out from the beginning of the string
    out_shift = num_str[-effective_shift:]
    # The part to be shifted in from the end of the string
    in_shift = num_str[:-effective_shift]
    
    # Return the result of the circular shift
    return out_shift + in_shift

print(circular_shift(12, 1))  # Outputs: "21"
print(circular_shift(12, 2))  # Outputs: "12"
```

In this script, we first convert the integer to a string to easily manipulate its digits. We then calculate the effective shift, which is the remainder of the shift divided by the number of digits in the string. This is because shifting by a number of digits larger than the number of digits in the string is equivalent to shifting by the remainder.

We then split the string into two parts: the part to be shifted out from the beginning of the string and the part to be shifted in from the end of the string. We return the result of the circular shift by concatenating these two parts.