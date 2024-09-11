```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be a positive floating point number.")
    
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part of the number
    decimal_part = number - integer_part
    
    return decimal_part


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.23))  # Output: 0.23
```