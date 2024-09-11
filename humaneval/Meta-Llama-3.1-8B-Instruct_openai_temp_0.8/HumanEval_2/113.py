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

    Raises:
        ValueError: If the given number is not positive.
    """
    if number <= 0:
        raise ValueError("Input number must be positive")

    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function called `truncate_number` which takes a positive floating point number as input and returns its decimal part. The function first checks if the input number is positive. If not, it raises a `ValueError`. If the input number is positive, it calculates the decimal part by subtracting the integer part from the number. The example usage demonstrates how to use this function with different inputs.