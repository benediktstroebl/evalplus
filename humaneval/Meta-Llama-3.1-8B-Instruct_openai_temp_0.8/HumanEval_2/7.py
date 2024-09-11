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

# Example use cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(10.8))  # Expected output: 0.8
```

This script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part. It uses the fact that subtracting the integer part of a number from the number itself leaves only the decimal part. This is implemented using the `int(number)` function, which truncates the decimal part of `number`. The example use cases demonstrate how the function works with different input values.