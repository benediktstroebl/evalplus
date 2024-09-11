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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))   # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(7))     # Output: 0.0
```

This script defines a function `truncate_number` that calculates the decimal part of a given floating point number by subtracting its integer part (which is obtained using the `int` function) from the number itself. The result is then printed to the console for demonstration purposes.