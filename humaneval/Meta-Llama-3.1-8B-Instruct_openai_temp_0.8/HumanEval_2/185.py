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
    """
    integer_part = int(number)
    return number - integer_part


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
print(truncate_number(2.7))  # Output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number, decomposes it into an integer part and a decimal part, and returns the decimal part. It then provides some example use cases to demonstrate the function's behavior.