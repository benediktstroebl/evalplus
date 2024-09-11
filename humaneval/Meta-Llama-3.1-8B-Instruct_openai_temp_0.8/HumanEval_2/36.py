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
        float: The decimal part of the given number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the built-in int() function to truncate the decimal part
    # and subtract it from the original number to get the decimal part
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.23))  # Output: 0.23
print(truncate_number(5.0))  # Output: 0.0
```

This script uses a simple mathematical operation to achieve the desired result. It subtracts the integer part (obtained by converting the number to an integer using `int()`) from the original number, thus leaving only the decimal part.