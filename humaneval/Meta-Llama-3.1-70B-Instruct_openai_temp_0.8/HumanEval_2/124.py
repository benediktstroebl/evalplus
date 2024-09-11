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
        float: The decimal part of the number.
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```
This script defines a function `truncate_number` that takes a floating-point number as input and returns its decimal part. The function works by subtracting the integer part of the number (obtained using the `int()` function) from the original number. The result is the decimal part of the number.