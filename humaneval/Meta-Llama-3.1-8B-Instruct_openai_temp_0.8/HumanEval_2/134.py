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
    integer_part = int(number)  # get the largest integer smaller than the number
    return number - integer_part  # subtract the integer part to get the decimal part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
```

This script defines the `truncate_number` function as described in the problem statement. It uses the built-in `int` function to get the largest integer smaller than the input number, and then subtracts this integer from the original number to get the decimal part. The function is then tested with some examples.