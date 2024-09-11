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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """

    # Check if the number is a positive floating point number
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError("The number must be a positive floating point number.")

    # Calculate the integer part of the number
    integer_part = int(number)

    # Calculate the decimal part of the number by subtracting the integer part from the number
    decimal_part = number - integer_part

    # Return the decimal part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
```