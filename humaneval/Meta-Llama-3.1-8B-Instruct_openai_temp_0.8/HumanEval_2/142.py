```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part.
    
    The decimal part is the leftover part after decomposing the number into
    an integer part (largest integer smaller than the given number) and decimals.
    
    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the given number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.23))  # Output: 0.23
```

In this code, we use the built-in `int()` function to get the integer part of the number, and then subtract this from the original number to get the decimal part. This works because the `int()` function truncates the decimal part, effectively rounding down to the nearest whole number.