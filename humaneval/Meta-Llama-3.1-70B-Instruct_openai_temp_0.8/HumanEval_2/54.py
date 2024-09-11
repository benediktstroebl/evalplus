```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): The input number to truncate.

    Returns:
        float: The decimal part of the input number.
    """
    if number < 0:
        raise ValueError("Input number must be positive.")

    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns the decimal part of the number. The function uses the fact that subtracting the integer part of a number (obtained using the `int()` function) from the original number leaves the decimal part.

Please note that this function does not handle negative numbers, as per the problem statement. If a negative number is passed to the function, it raises a `ValueError`.