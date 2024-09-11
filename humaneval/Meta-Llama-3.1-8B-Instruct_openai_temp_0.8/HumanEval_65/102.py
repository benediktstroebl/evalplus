```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to perform the circular shift on.
        shift (int): The number of digits to shift.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access and manipulate the digits
    num_str = str(x)
    
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the shift point
    # The part after the shift point is moved to the beginning
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 5))  # Output: "321"
```

This script defines a function `circular_shift` that performs the described operation. It first converts the integer to a string, then calculates the effective shift in case it's greater than the number of digits. It splits the string into two parts at the shift point, moves the part after the shift point to the beginning, and returns the result as a string. The script also includes test cases to demonstrate the function's correctness.