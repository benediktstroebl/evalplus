```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
   0
   5

    Numpy float min value is negative finite 5e-12146314, 
    so the maximum decimal part is very small ( around 4e-9).
    """
    number %= 1e%10**(9)
    return number
```