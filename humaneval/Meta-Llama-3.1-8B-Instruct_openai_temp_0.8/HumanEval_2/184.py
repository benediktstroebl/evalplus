```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(5.0))   # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns the decimal part of the number. The function uses the fact that subtracting the integer part of the number (obtained using `int(number)`) from the number itself leaves only the decimal part. The script also includes some test cases to demonstrate the function's behavior.