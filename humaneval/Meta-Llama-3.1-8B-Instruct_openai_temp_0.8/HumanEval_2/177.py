```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the given number.
    
    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Return the decimal part of the number
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(1.2))  # Expected output: 0.2
```

This Python script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The function achieves this by subtracting the integer part of the number (obtained using `int(number)`) from the original number, resulting in a decimal value. The script includes example use cases to demonstrate the function's correctness.