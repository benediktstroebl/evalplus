### Circular Shift Function
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
    # Convert the integer to a string to easily operate on its digits
    x_str = str(x)
    
    # Calculate the effective shift, considering the number of digits
    effective_shift = shift % len(x_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return x_str[::-1]
    
    # Split the string into two parts at the effective shift position
    first_part = x_str[-effective_shift:]
    second_part = x_str[:-effective_shift]
    
    # Combine the two parts in reverse order to get the shifted string
    shifted_str = first_part + second_part
    
    return shifted_str

# Test cases
print(circular_shift(12, 1)) # Output: "21"
print(circular_shift(12, 2)) # Output: "21"
```
This script defines the `circular_shift` function, which takes an integer `x` and the number of digits to shift `shift` as arguments. The function first converts the integer to a string, then calculates the effective shift considering the number of digits. It splits the string into two parts at the effective shift position and combines them in reverse order to get the shifted string. If the shift is equal to the number of digits, it returns the reversed string. The script also includes test cases to verify the function's correctness.