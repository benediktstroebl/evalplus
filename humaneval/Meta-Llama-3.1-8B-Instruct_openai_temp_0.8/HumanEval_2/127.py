### Truncating a Number to its Decimal Part

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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number as input, and returns its decimal part. It achieves this by subtracting the integer part of the number from the original number, effectively removing the whole number from the decimal part. The result is then returned.