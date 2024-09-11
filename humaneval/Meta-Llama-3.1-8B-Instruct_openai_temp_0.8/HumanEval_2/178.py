```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # We use the built-in math.floor function to get the largest integer smaller than the number
    # Then we subtract this integer from the original number to get the decimal part
    import math
    return number - math.floor(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.123))  # Expected output: 0.123
```

This script defines a function `truncate_number` that takes a floating point number as input and returns its decimal part. The function uses the `math.floor` function to get the largest integer smaller than the number, and then subtracts this integer from the original number to get the decimal part.