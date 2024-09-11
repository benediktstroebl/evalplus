```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
    number: A positive floating point number.

    Returns:
    The decimal part of the number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)  # subtracting the integer part from the number


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script defines a function `truncate_number` which calculates the decimal part of a given floating point number. It does this by subtracting the integer part of the number (obtained using `int(number)`) from the number itself. The result is the decimal part of the number. The script includes a docstring that explains how to use the function, including an example usage.