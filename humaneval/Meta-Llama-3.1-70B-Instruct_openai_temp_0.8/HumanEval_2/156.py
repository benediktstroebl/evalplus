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
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive float.")
    return number - int(number)


if __name__ == "__main__":
    # Test cases
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(10.234))  # Expected output: 0.234
    print(truncate_number(0.9876))  # Expected output: 0.9876
```