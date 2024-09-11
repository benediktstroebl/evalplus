```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.8))  # Expected output: 0.8
print(truncate_number(5.0))   # Expected output: 0.0
```

This code defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The function works by subtracting the integer part of the number from the original number. The integer part is obtained using the built-in `int` function, which truncates the decimal part. The result is then returned by the function.