```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it decomposes it into an integer part
    (largest integer smaller than given number) and decimals (leftover part always smaller than 1).
    
    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.
    
    Returns:
    float: The decimal part of the number.
    
    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # We use the math.floor function to get the largest integer smaller than the given number
    integer_part = math.floor(number)
    # To get the decimal part, we subtract the integer part from the original number
    decimal_part = number - integer_part
    return decimal_part

import math

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.27))  # Output: 0.27
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The function uses the `math.floor` function to get the largest integer smaller than the given number, and then subtracts this integer from the original number to get the decimal part. The script also includes example use cases to demonstrate how to use the function.