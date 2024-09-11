```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5

    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.7))  # Expected output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number as input. It calculates the decimal part by subtracting the integer part (obtained using the built-in `int` function) from the original number. The result is then printed to the console using the `print` function.