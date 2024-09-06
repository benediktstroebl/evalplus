```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # Perform integer division to remove decimals
    integer_part = number // math.floor(number)
    # Remove the decimal part
    decimal_part = number % math.floor(number)
    # Return the decimal part
    return float(integer_part) + float(decimal_part)
```