```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Use the built-in math.floor function to get the largest integer smaller than the number
    integer_part = math.floor(number)
    
    # Calculate the decimal part by subtracting the integer part from the original number
    decimal_part = number - integer_part
    
    return decimal_part

import math

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
print(truncate_number(4.0))  # Output: 0.0
```