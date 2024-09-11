```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
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
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
```

This script defines the `truncate_number` function as specified, which takes a positive floating point number as input and returns its decimal part. The function uses integer division to truncate the number, and then subtracts the truncated integer from the original number to get the decimal part. The script also includes example test cases to demonstrate the function's usage.