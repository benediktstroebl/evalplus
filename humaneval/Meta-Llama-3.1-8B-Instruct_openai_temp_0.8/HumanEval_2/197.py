```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
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

# Example use case
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
print(truncate_number(5.0))  # Output: 0.0
```

This script uses Python's built-in `int()` function to convert the number to an integer, which effectively truncates the decimal part and then subtracts that value from the original number to get the decimal part. The example use cases demonstrate the function's usage with different inputs.