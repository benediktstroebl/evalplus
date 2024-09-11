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
    if number < 0:
        raise ValueError("Input number must be positive")

    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
print(truncate_number(7.0))  # Output: 0.0
```