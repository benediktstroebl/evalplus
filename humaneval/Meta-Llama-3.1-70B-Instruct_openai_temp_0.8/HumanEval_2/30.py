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
    if number < 0:
        raise ValueError("Input number should be a positive floating point number")

    return number - int(number)


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.2))  # Expected output: 0.2
print(truncate_number(5))  # Expected output: 0.0
```