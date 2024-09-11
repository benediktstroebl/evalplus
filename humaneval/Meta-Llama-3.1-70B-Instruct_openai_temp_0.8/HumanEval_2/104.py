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
    """
    if number < 0:
        raise ValueError("Input number must be non-negative.")
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - int(number)
    
    return decimal_part


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(7))  # Output: 0.0
try:
    print(truncate_number(-1.8))  # Raises ValueError
except ValueError as e:
    print(e)
```