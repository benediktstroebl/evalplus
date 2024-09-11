```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5

    Args:
        number (float): A positive floating point number

    Returns:
        float: The decimal part of the number
    """
    return number - int(number)


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
print(truncate_number(2.75))  # Output: 0.75
```

This script defines a function `truncate_number` that takes a floating point number as input, subtracts its integer part (obtained by `int(number)`) from the number itself to obtain the decimal part, and returns this decimal part. The example usage demonstrates how to use this function with different inputs.