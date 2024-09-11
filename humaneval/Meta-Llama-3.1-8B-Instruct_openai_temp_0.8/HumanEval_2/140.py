### Truncate Number to Decimal Part

Here's a Python function that truncates a given floating point number to its decimal part:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it decomposes it into
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
    # Subtract the integer part from the number to get the decimal part
    return number - int(number)


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
print(truncate_number(5.0))  # Output: 0.0
```