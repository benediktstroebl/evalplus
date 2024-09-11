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
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.2))  # Output: 0.2
print(truncate_number(10.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating-point number, subtracts its integer part, and returns the decimal part. The function is then tested with a few examples to demonstrate its correctness.