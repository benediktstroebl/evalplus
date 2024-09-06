```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal_part = 0.0
    while integer_part = floor(number / 10)

    number = number % 10
    return float(decimal_part + integer_part * 10)
```