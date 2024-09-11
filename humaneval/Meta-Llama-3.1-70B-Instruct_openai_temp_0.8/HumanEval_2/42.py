```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number: A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Raises:
        ValueError: If the input number is not positive.

    >>> truncate_number(3.5)
    0.5
    """
    if number <= 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part of the number
    integer_part = int(number)

    # Calculate the decimal part of the number
    decimal_part = number - integer_part

    return decimal_part

# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.23))  # Output: 0.23
    print(truncate_number(0.99))  # Output: 0.99
    try:
        print(truncate_number(-0.99))  # Raises ValueError
    except ValueError as e:
        print(e)  # Output: Input number must be positive
```