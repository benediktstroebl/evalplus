```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.98))  # Output: 0.98
print(truncate_number(10.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input, subtracts its integer part from it, and returns the decimal part. The example usage at the bottom demonstrates how to use this function with different inputs.