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

# Testing the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(5.0))  # Expected output: 0.0
```

This Python script defines the `truncate_number` function which takes a positive floating-point number as input, decomposes it into its integer and decimal parts, and returns the decimal part. The decimal part is obtained by subtracting the integer part (converted to an integer using `int(number)`) from the original number. The script also includes some test cases to demonstrate the function's correctness.