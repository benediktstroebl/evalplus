```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    true
    true
    
    >>> truncate_number(0.0)
    0.0
    true 
    >>> truncate_number(-3.0) == 0.0
    true
    reason: the number is negative, but it should return a non-positive number.