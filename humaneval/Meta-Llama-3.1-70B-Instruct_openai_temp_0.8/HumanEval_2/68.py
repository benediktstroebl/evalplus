```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10)
    0.0
    >>> truncate_number(10.234)
    0.234
    """
    if number < 0:
        raise ValueError("Input number must be non-negative")
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10))   # Outputs: 0.0
print(truncate_number(10.234))  # Outputs: 0.234
```