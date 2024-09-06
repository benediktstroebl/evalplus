```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    >>> return 0.5 if number < 2
   5
    """ Test case 
    assert truncate_number(3.5) == 0.5
    assert truncate_number(-3.5) == -3
   5
    assert truncate_number(0.3) == 0.2
    assert truncate_number('3.5') == 0.5
    assert truncate_number('a.3') == 3
5
    """ A good job!