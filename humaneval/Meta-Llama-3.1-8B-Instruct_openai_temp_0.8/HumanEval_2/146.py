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
print(truncate_number(4.8))  # Expected output: 0.8
print(truncate_number(5))    # Expected output: 0.0
```

This script works by subtracting the integer part of the number from the number itself. This effectively gives us the decimal part of the number. The `int(number)` function is used to truncate the number to its integer part.