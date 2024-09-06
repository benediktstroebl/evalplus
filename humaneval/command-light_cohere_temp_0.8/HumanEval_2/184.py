```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 if number <= 1 else
    important if number < 0 else
    1 - (number % 1) if number > 1 else

    """
    return 1 - (number % 1)
```