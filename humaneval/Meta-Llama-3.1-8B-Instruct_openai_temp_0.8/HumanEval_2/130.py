```python
def truncate_number(number: float) -> float:
    """
    Decompose a positive floating point number into its integer and decimal parts.
    Return the decimal part.

    Args:
    number (float): A positive floating-point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(2.75))  # Expected output: 0.75
```

This Python script defines a function `truncate_number` that takes a positive floating-point number, subtracts its integer part (obtained using `int(number)`) from it, and returns the result as the decimal part of the number. The `int(number)` operation truncates the decimal part, and then subtracting it from the original number leaves the decimal part. The function is then tested with some example inputs to demonstrate its correctness.