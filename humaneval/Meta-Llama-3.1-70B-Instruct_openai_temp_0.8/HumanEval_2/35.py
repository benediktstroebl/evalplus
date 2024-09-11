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
        ValueError: If the input number is not a positive float.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """

    # Check if the input is a positive float
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive float.")

    # Use the modulo operator to get the decimal part
    # The modulo operator returns the remainder of the division of the number by 1
    decimal_part = number % 1

    return decimal_part


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
print(truncate_number(7.0))  # Output: 0.0
```
This script defines the `truncate_number` function, which calculates the decimal part of a given positive floating point number. It first checks if the input is a positive float, and if not, it raises a `ValueError`. Then it uses the modulo operator to get the decimal part of the number. The modulo operator returns the remainder of the division of the number by 1, which is the decimal part. The function returns this decimal part.