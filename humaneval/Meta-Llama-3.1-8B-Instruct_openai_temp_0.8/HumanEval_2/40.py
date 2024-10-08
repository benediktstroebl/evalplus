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
    
    Examples:
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10.75)
    0.75
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
```

In this script, we subtract the integer part of the input number (obtained using `int(number)`) from the number itself to obtain its decimal part. The result is then returned.