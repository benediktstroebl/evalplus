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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative number.")
    
    # Use the modulo operator to get the decimal part
    decimal_part = number % 1
    
    return decimal_part


# Example usage:
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10.2))  # Outputs: 0.2
print(truncate_number(7))  # Outputs: 0.0
```