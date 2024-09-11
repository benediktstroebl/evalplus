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
    # Check if number is positive
    if number < 0:
        raise ValueError("Number must be a positive floating point number.")

    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
print(truncate_number(0.7))  # Output: 0.7
```