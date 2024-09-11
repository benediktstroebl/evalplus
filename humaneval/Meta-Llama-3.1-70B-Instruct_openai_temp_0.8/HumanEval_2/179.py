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
print(truncate_number(123.456))  # Output: 0.456
```

This script defines the `truncate_number` function, which takes a positive floating point number and returns its decimal part. It first checks if the input number is negative and raises a `ValueError` if it is. Then, it calculates the decimal part by subtracting the integer part (obtained using the `int()` function) from the original number. Finally, it provides example usage of the function.