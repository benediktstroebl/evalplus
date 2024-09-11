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
    if not isinstance(number, float) or number < 0:
        raise ValueError("Input must be a non-negative float.")

    return number - int(number)

# Example use case
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.2))  # Output: 0.2
    print(truncate_number(5.0))  # Output: 0.0
```