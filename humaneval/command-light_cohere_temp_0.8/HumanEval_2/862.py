```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    >>> num = 3.5
   
   
        integer part = int(number)
    >>> float('{integer part}') <= number
    True
    >>> float('{integer part}'.5) > number
    False
    >>> decimal = number - float('{integer part}')
    >>> int(decimal)
    0
    >>> int(number - 0) == int(number)
    True
    """
    return number - float('{integer part}')
```