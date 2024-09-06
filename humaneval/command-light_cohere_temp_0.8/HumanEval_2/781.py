```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    number = float(number)
    if number < 0:
        return -1e18
    elif number == 0:
        return 0
    else:
        return 1e18 - number
```