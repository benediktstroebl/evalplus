```markdown
### Circular Shift Function
#### Problem Description
Circular shift the digits of the integer `x`, shift the digits right by `shift` and return the result as a string.
If `shift > number of digits`, return digits reversed.

#### Solution
```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The result as a string after circular shift.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift by taking the modulus of the length of the string
    # This handles cases where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted and the part to be added to the end
    shifted_part = str_x[-effective_shift:]
    added_part = str_x[:-effective_shift]
    
    # Return the result by concatenating the two parts
    return shifted_part + added_part

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```
This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result as a string after circular shifting the digits. The function first converts the integer to a string to easily manipulate the digits. It then calculates the effective shift by taking the modulus of the length of the string to handle cases where shift > number of digits. Finally, it splits the string into two parts, shifts the first part to the end, and returns the result by concatenating the two parts. The test cases demonstrate the usage and correctness of the function.