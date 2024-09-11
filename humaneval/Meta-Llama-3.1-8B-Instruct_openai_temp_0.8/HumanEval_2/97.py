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

    >>> truncate_number(3.5)
    0.5
    """
    # We subtract the integer part from the original number to get the decimal part
    decimal_part = number - int(number)
    return decimal_part


# Example use cases
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(4.0))  # Outputs: 0.0
print(truncate_number(3.75))  # Outputs: 0.75
```

In this script, we define a function `truncate_number` that takes a positive floating point number, subtracts its integer part (obtained by casting to an integer), and returns the result, which is the decimal part of the original number. The example use cases demonstrate the function's behavior for different inputs.