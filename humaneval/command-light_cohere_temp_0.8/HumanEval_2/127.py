```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 1
   0
    >>> return 0.375 if number < 3
   5
    >>> return 0.25 if number < 0
   5
    >>> return 0.9999 if number < 10
   5
    """