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
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(7.23))  # Expected output: 0.23
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The function works by subtracting the integer part (which is obtained by casting the number to an integer) from the original number. This effectively removes the integer part and leaves only the decimal part. The result is then printed to the console to demonstrate the function's behavior.