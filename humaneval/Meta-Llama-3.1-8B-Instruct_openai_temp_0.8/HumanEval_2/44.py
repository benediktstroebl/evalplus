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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Should print 0.5
```

In this script, we're using the built-in `int()` function in Python, which truncates a floating point number to the nearest integer. We then subtract this integer from the original number to get the decimal part. This approach assumes that the input is a positive floating point number, as specified in the problem statement.