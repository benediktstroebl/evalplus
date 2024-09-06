```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)
    a 0.5
>>> int(truncate_number(3.5)) == 300

>>> 1.000 decimal_part(3.5) < 1
 decimal_part(0.0) < 1

    True
```