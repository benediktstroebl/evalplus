```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the given number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example use cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(2.0))  # Expected output: 0.0
print(truncate_number(5.75))  # Expected output: 0.75
```

This Python function `truncate_number` calculates the decimal part of a given positive floating point number by subtracting the integer part from the number itself.