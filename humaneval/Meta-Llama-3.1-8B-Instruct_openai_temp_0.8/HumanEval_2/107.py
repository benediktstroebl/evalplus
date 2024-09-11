```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than the given number) and decimals 
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

# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.78))  # Expected output: 0.78
print(truncate_number(2.0))  # Expected output: 0.0
```

This script defines a function `truncate_number` that calculates the decimal part of a given number. It then tests the function with a few example cases. The decimal part is calculated by subtracting the integer part of the number from the original number. This is done using the `int(number)` function, which returns the largest integer smaller than the given number.