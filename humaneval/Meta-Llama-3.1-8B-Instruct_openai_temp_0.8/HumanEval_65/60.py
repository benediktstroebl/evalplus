```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits

    Returns:
    str: The shifted integer as a string
    """
    # Convert the integer to a string to easily access and manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the part to be shifted to the end and the part to remain at the beginning
    first_part = x_str[-effective_shift:]
    second_part = x_str[:-effective_shift]
    
    # Combine the two parts in the correct order to get the shifted string
    shifted_str = first_part + second_part
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts `x` to a string, calculates the effective shift, splits the string into two parts, and combines them in the correct order to get the shifted string. The function returns the shifted string. The script includes docstrings and test cases to demonstrate the function's behavior.