```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the integer part using the math.floor function
    import math
    integer_part = math.floor(number)
    
    # Calculate the decimal part by subtracting the integer part from the original number
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
```

This script uses the built-in `math.floor` function to calculate the largest integer smaller than the given number. It then subtracts this integer part from the original number to get the decimal part. The function is tested with two examples to demonstrate its functionality.