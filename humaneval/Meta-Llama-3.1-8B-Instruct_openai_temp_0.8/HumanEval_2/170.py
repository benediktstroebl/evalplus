```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(1.25))  # Expected output: 0.25
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is calculated by subtracting the integer part of the number from the number itself. The `int(number)` expression truncates the decimal part of the number, effectively rounding down to the nearest whole number.