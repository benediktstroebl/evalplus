```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.0))  # Expected output: 0.0
print(truncate_number(5.25))  # Expected output: 0.25
```

This script defines a function `truncate_number` that takes a positive floating point number as input, calculates its decimal part by subtracting its integer part, and returns this decimal part. The test cases at the end verify that the function works correctly.