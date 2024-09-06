```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    if number <= 0:
        return 0.0
    elif number == 1:
        return 1.0
    else:
        # Decompose the number into integer and decimal parts
        decimal = number % 1.0
        integer = math.ceil(decimal)
        # Return integer part
        return integer + decimal
```