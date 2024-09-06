```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    >>> return 0.5 if number < 1
   
    >>> return 0.1 if number < 0.2
   0.5 if number0
        COUNT(number) <= 1
    1.0 if number < 2
   0
        else:
        return number - 1
```