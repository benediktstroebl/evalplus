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

    Raises:
        ValueError: If the number is not a positive floating point number.
    """
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive float.")

    # The decimal part can be obtained by subtracting the integer part from the number.
    # The integer part can be obtained using the int() function, which truncates the decimal part.
    decimal_part = number - int(number)

    return decimal_part

# Example use cases:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))  # Output: 0.0
```