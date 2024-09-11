```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the number.
    
    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the built-in math.floor function to get the largest integer smaller than the given number
    integer_part = math.floor(number)
    
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

import math

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
print(truncate_number(7.23))  # Output: 0.23
```

This script defines a function `truncate_number` that takes a positive floating point number as input, decomposes it into its integer and decimal parts, and returns the decimal part. The decimal part is calculated by subtracting the integer part from the original number. The script also includes a test section to demonstrate the function's behavior.