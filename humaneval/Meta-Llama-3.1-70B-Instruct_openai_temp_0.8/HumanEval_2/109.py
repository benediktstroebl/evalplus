```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number should be positive")
    integer_part = int(number)  # Get the integer part
    decimal_part = number - integer_part  # Subtract integer part from the number
    return decimal_part


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.23))  # Output: 0.23
print(truncate_number(5))  # Output: 0.0
try:
    print(truncate_number(-1.1))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Input number should be positive
```