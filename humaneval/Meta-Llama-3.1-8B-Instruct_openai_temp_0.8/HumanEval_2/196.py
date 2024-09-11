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
    # Use the modulo operator to get the remainder after dividing by 1
    # This will be the decimal part of the number
    return number % 1


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.2))  # Output: 0.2
print(truncate_number(5.7))  # Output: 0.7
```

This script uses the modulo operator (`%`) to get the decimal part of a given number. The `%` operator returns the remainder of the division of the number by 1, which is the decimal part.