```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): The input number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script defines the `truncate_number` function, which calculates the decimal part of a given positive floating point number by subtracting its integer part from the original number. The `int(number)` function returns the largest integer smaller than or equal to the given number, effectively removing the decimal part. The function is then tested with two examples.