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
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.23))  # Expected output: 0.23
```

This Python script defines a function called `truncate_number` which takes a floating point number as input, calculates the decimal part by subtracting the integer part (obtained using the `int()` function) from the original number, and returns the result. The script also includes example use cases.