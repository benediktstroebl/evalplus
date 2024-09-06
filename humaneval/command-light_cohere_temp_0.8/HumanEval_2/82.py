```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer = []
    while number > 0:
        number -= int(number)
        integer.append(number)
    decimal = number
    return float(''.join(decimal)) if decimal != 0 else float('') + integer[0]
```