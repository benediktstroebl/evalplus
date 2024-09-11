```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    :param number: A positive floating point number.
    :return: The decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if not isinstance(number, float) or number < 0:
        raise ValueError("Input must be a positive floating point number")

    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.99))  # Output: 0.99
print(truncate_number(7))  # Output: 0.0
```