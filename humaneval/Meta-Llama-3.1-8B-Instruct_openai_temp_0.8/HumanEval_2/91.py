```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.
    
    Returns:
    float: The decimal part of the input number.
    
    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    # Use the math.floor function to get the largest integer smaller than the number
    integer_part = math.floor(number)
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    return decimal_part

import math
# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This script uses the `math.floor` function to decompose the number into an integer part and a decimal part, and then returns the decimal part. The decimal part is calculated by subtracting the integer part from the original number.