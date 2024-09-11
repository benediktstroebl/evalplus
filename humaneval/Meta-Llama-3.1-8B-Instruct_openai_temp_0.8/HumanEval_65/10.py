```markdown
### Circular Shift Function

This Python script defines a function `circular_shift` that performs a circular shift on the digits of an integer. The shift is applied to the right and the result is returned as a string.

#### Code

```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits to the right.
    
    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily extract and manipulate digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Perform the circular shift using string slicing
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

#### Explanation

This code works by first converting the input integer to a string. It then calculates the effective shift by taking the modulus of the shift with the number of digits in the string. This handles the case where the shift is greater than the number of digits.

The circular shift is then performed using string slicing. The `[-effective_shift:]` slice extracts the last `effective_shift` characters from the string, and the `[:-effective_shift]` slice extracts all characters except the last `effective_shift` characters. These two slices are then concatenated to form the shifted string.

Finally, the shifted string is returned as the result.