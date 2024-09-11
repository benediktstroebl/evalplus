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
    float: The decimal part of the given number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```

This script defines a function `truncate_number` that takes a positive floating point number as input, subtracts its integer part to get the decimal part, and returns the result. The script also includes docstrings to describe the function's behavior and provides test cases to verify the function's correctness.