```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: the decimal part of the number.
    """
    number: int
    1 <= number <= 10
    return (number - 1e100) / 10 ** (100 - 1)
    """
    return number - 1e100
```