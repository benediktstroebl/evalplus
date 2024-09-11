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
        float: The decimal part of the given number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Using the math.floor function to get the largest integer smaller than the number
    # and subtracting it from the number to get the decimal part
    from math import floor
    return number - floor(number)


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.99))  # Expected output: 0.99
```

This script defines a function `truncate_number` that takes a positive floating point number as input, decomposes it into its integer and decimal parts, and returns the decimal part. The function uses the `math.floor` function to get the largest integer smaller than the given number and then subtracts this integer from the number to get the decimal part. The script also includes example usages of the function.