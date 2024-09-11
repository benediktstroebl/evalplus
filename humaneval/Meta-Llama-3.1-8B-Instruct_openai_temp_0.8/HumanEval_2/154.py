```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))   # Output: 0.5
print(truncate_number(5.0))   # Output: 0.0
print(truncate_number(1.75))  # Output: 0.75
```

This script uses the built-in `int()` function to extract the integer part of the number, then subtracts this integer from the original number to get the decimal part. The result is then returned. The example usage section demonstrates how to use the `truncate_number()` function with various inputs.