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
    return number - int(number)


# Example usage:
print(truncate_number(3.5))   # Output: 0.5
print(truncate_number(5.0))   # Output: 0.0
print(truncate_number(7.23))  # Output: 0.23
```

This Python script defines a function `truncate_number` that takes a positive floating point number as input and returns the decimal part of the number. The function uses simple subtraction to achieve this by subtracting the integer part (obtained using the `int` function) from the original number. The result is the decimal part of the number.