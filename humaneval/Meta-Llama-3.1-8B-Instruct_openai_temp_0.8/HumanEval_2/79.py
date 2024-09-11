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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # We use the built-in math.floor function to find the largest integer smaller than the given number.
    # Then we subtract this integer from the original number to get the decimal part.
    return number - math.floor(number)


import math

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.123))  # Output: 0.123
print(truncate_number(10.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a floating point number as input, calculates the decimal part by subtracting the largest integer smaller than the number from it, and returns the result. The `math.floor` function is used to find this integer. The script also includes example usage of the function.