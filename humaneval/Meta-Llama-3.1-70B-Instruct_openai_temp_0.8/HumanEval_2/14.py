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
    # Use the modulo operator to get the decimal part of the number
    # This works by subtracting the integer part (obtained using int()) from the number
    decimal_part = number - int(number)
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```