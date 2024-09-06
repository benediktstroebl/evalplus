```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Returns the decimal part of the number.
    >>> assert truncate_number(3.5) == 0.5
   
    earlier of
 basic tests pass, and you can easily add more advanced tests if needed.