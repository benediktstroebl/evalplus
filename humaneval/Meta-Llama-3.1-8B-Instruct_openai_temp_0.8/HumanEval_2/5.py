```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.27))  # Expected output: 0.27
print(truncate_number(5))  # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number, subtracts its integer part to get the decimal part, and returns it. The function is then tested with a few examples.