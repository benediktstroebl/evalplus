### Truncate Number Function
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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))   # Output: 0.0
```
This script defines the `truncate_number` function, which takes a positive floating point number as input and returns its decimal part. The function works by subtracting the integer part of the number from the number itself. This is done using the built-in `int()` function, which truncates the decimal part.