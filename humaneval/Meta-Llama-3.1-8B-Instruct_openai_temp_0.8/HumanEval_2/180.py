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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(12.7))  # Output: 0.7
print(truncate_number(5.0))  # Output: 0.0
```

In this script, we use the built-in `int()` function to truncate the integer part of the given number. The decimal part is then obtained by subtracting the integer part from the original number.