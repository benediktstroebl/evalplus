```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The result of the circular shift
    """
    # Convert the integer to a string to easily access and manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    first_part = str_x[:-effective_shift]
    second_part = str_x[-effective_shift:]
    
    # Reverse the first part if the shift is greater than the number of digits
    if effective_shift > len(str_x) // 2:
        first_part = first_part[::-1]
    
    # Combine the two parts in the correct order to get the result
    result = second_part + first_part
    
    # Return the result as a string
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift, splits the string into two parts, and combines them in the correct order to get the result. The function includes comments and docstrings to explain its behavior and usage. The script also includes test cases to demonstrate the function's correctness.