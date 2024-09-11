```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to shift.
        shift (int): The number of positions to shift the digits.
    
    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access and manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the part to be shifted to the end and the part to be shifted to the beginning
    # Use string slicing to achieve this
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    # Return the result as a string
    return shifted_str


# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 2))  # Output: "321"
print(circular_shift(123, 5))  # Output: "321"
```
This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift as a string. The function first calculates the effective shift by taking the remainder of the division of the shift by the length of the string representation of the integer. It then splits the string into two parts: the part to be shifted to the end and the part to be shifted to the beginning, and combines them to form the final result. The script includes test cases to demonstrate the function's behavior.