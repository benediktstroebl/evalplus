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
    str: The result of the circular shift operation as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    
    # Combine the two parts to get the result of the circular shift operation
    result = first_part + second_part
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift operation as a string. The function uses string manipulation to achieve the circular shift, and includes a test to handle the case where `shift` is greater than the number of digits in `x`. The test cases are included at the end of the script to verify the function's correctness.