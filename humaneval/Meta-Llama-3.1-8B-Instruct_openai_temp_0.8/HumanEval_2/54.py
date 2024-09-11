```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
    number: A positive floating point number.

    Returns:
    The decimal part of the number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.123))  # Expected output: 0.123
```

This script uses the built-in `int()` function to truncate the number to its integer part, and then subtracts this integer part from the original number to get the decimal part. This solution works because in Python, the `int()` function truncates the decimal part of a floating point number.