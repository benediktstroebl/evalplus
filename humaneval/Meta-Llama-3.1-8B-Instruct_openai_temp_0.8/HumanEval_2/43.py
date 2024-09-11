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
print(truncate_number(5.3))  # Output: 0.3
print(truncate_number(10.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part. It uses the trick of subtracting the integer part of the number from the original number to get the decimal part. The function is tested with sample inputs to demonstrate its correctness.