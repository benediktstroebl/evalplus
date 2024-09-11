```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.8))  # Output: 0.8
print(truncate_number(5.0))  # Output: 0.0
```

This script works by subtracting the integer part of the number (obtained using the `int()` function) from the original number. This effectively leaves us with the decimal part. The script also includes example usage to demonstrate how the function can be used.