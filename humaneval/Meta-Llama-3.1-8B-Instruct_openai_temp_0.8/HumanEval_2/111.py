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
    # Use the built-in int function to truncate the number to the nearest integer
    # The decimal part will be the difference between the original number and the truncated number
    return number - int(number)


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(10.7))  # Expected output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number as input, truncates it to the nearest integer using the built-in `int` function, and then returns the decimal part by subtracting the truncated number from the original number. The function is then tested with several examples to verify its correctness.