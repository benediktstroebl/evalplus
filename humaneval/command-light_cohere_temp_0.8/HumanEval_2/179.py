```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> assert truncate_number(3.5) == 0.0
   
   
   
  numeral part is the largest integer smaller than the given number, and the decimal part is the leftover.
```