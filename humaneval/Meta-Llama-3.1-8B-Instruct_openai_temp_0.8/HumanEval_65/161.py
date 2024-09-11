```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of digits to shift.
    
    Returns:
    str: The shifted integer as a string.
    """
    # Convert integer to string to easily manipulate digits
    str_x = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the end and the rest
    part_to_shift = str_x[-effective_shift:]
    rest_of_string = str_x[:-effective_shift]
    
    # Shift the digits by concatenating the two parts in reverse order
    shifted_string = part_to_shift + rest_of_string
    
    return shifted_string

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It first converts the integer to a string to easily manipulate its digits. Then, it calculates the effective shift by taking the remainder of the shift value divided by the number of digits in the string. This ensures that if the shift value is greater than the number of digits, the function behaves as intended. Finally, it splits the string into two parts, shifts the digits by concatenating these parts in reverse order, and returns the result as a string. The function is then tested with the provided example inputs.