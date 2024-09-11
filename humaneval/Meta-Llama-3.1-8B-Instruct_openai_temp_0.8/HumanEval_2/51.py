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
        float: The decimal part of the number.
    """
    return number - int(number)


# Test cases
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(2.0))  # Output: 0.0
print(truncate_number(5.75))  # Output: 0.75
```

This script defines the `truncate_number` function, which subtracts the integer part of the input number from the number itself to get the decimal part. It then includes test cases to demonstrate the function's behavior.