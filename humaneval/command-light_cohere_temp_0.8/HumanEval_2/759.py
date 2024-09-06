```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals. 
    Return the region part of the decimal number.
    >>> truncate_number(3.5) == 0.2
>>> truncate_number(0.6) == 0.3
>>> truncate_number(1.5) == 1
```