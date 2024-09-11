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
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.2))  # Output: 0.2
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It uses the built-in `int` function to truncate the integer part of the number and then subtracts it from the original number to get the decimal part. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of usage.