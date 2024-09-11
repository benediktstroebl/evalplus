```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it decomposes the number into
    the integer part (largest integer smaller than the given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10.7))  # Outputs: 0.7
```

In this script, we use the built-in `int()` function to truncate the integer part of the number, and then subtract this from the original number to get the decimal part. This works because the `int()` function returns the largest integer smaller than the given number, as specified in the problem statement.