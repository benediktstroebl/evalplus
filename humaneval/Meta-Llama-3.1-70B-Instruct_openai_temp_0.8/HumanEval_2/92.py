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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative number")

    # Use the built-in math.modf function to split the number into integer and fractional parts
    import math
    _, decimal_part = math.modf(number)

    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(5))  # Expected output: 0.0
```