```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.123))  # Output: 0.123
```

In this script, we use the built-in `int()` function to truncate the integer part of the number, and then subtract this integer from the original number to get the decimal part. This works because the `int()` function returns the largest integer smaller than the given number.