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

# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(2.0))  # Expected output: 0.0
print(truncate_number(1.25)) # Expected output: 0.25
```

This script uses Python's built-in `int(number)` function to truncate the decimal part of the input number. The function then subtracts the truncated integer from the original number, leaving only the decimal part.