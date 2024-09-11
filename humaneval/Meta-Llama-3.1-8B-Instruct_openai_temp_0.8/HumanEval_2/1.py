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
print(truncate_number(2.8))  # Output: 0.8
print(truncate_number(1.0))  # Output: 0.0
```

This script defines the function `truncate_number` as described in the problem. It calculates the decimal part by subtracting the integer part (`int(number)`) from the input number.