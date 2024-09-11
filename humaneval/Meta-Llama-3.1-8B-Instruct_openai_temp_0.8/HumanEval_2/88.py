### Truncate Number Script
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
    # Calculate the integer part using math module's floor function
    from math import floor
    integer_part = floor(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part if decimal_part > 0 else 0

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.9))  # Output: 0.9
print(truncate_number(6.0))  # Output: 0.0
```

This script defines a function called `truncate_number` that takes a positive floating point number as input and returns its decimal part. If the decimal part is zero, it returns zero as specified in the problem. The function uses the `math.floor` function to calculate the integer part of the number and then subtracts this integer part from the original number to get the decimal part. The script also includes test cases to demonstrate the function's correctness.