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
    # Ensure the number is positive
    if number < 0:
        raise ValueError("Input number must be positive")

    # Calculate the decimal part
    decimal_part = number - int(number)

    return decimal_part

# Example usage
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
print(truncate_number(123.0))  # Output: 0.0
```