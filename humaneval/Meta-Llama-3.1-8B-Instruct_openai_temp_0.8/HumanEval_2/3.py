```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the integer part of the number
    integer_part = int(number)
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.1234))  # Output: 0.1234
```

This script defines the `truncate_number` function, which takes a positive floating point number as input and returns its decimal part. The function works by first calculating the integer part of the number using the `int()` function, then subtracting this integer part from the original number to get the decimal part. The script includes two test cases to verify that the function works correctly.