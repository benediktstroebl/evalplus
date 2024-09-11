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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)


# Testing the function
print(truncate_number(3.5))   # Expected output: 0.5
print(truncate_number(7.23))  # Expected output: 0.23
print(truncate_number(2.0))   # Expected output: 0.0
```

In this script, the `truncate_number` function takes a floating point number as input and returns the decimal part by subtracting the integer part from the number. The integer part is obtained by casting the number to an integer using the `int()` function. The script also includes some test cases to demonstrate the function's behavior.