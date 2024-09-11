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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative number")

    # Use the built-in modulo operator to get the decimal part
    return number % 1


# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.75))  # Output: 0.75
    print(truncate_number(2))  # Output: 0.0
```