```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    # Ensure the number is positive
    if number < 0:
        raise ValueError("Input number must be positive")

    # Calculate the decimal part
    decimal_part = number - int(number)

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This script defines the `truncate_number` function, which takes a positive floating-point number as input and returns its decimal part. It first checks if the input number is positive and raises a `ValueError` if it's not. Then, it calculates the decimal part by subtracting the integer part (obtained using the `int()` function) from the original number. Finally, it returns the decimal part.

You can run this script and use the `truncate_number` function to get the decimal part of any positive floating-point number.