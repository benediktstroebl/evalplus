```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.9))  # Expected output: 0.9
print(truncate_number(5.0))  # Expected output: 0.0
```