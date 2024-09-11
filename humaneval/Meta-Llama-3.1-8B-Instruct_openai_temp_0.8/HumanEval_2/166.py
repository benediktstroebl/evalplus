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


# Testing the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.987))  # Output: 0.987
```

This script defines the `truncate_number` function, which calculates the decimal part of a given number by subtracting its integer part from the original number. It then tests the function with two examples.