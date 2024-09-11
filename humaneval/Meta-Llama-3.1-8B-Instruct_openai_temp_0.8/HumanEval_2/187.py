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

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.75))  # Expected output: 0.75
print(truncate_number(5))  # Expected output: 0.0
```

This script defines a function `truncate_number` that calculates the decimal part of a given floating-point number by subtracting its integer part from the number itself. It then tests this function with a few examples.