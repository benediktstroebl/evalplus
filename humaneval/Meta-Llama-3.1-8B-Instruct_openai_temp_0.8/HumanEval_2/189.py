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
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.23))  # Expected output: 0.23
print(truncate_number(5.0))  # Expected output: 0.0
```

This script uses the fact that in Python, `int(number)` truncates the decimal part of `number`. Therefore, subtracting `int(number)` from `number` results in the decimal part of `number`.