```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)
    """ 0.25
    3."""

def test_truncate_number():
    assert truncate_number(3.5) == 0.3
    assert truncate_number(-1.5) == -3.7  #assert truncate_number(0.1) == 0.0  #assert truncate_number(-3.0) == -3.5 
```