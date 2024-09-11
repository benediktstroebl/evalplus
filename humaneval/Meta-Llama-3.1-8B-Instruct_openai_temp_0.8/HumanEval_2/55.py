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
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function called `truncate_number` that takes a float as input, subtracts its integer part, and returns the fractional part. The fractional part is the remainder when the input float is divided by 1. The script also includes example use cases to demonstrate how the function works.