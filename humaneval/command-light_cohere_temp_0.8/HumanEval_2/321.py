```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    >>> return 0.5 if x < 0
    < 2.25 else: return x // 1.25
   + 
    """ python"""
def test_truncate_number():
    assert truncate_number(2.5) == 0.5
    assert truncate_number(3.0) == 0.8
    assert truncate_number(-3.0) == -0.2 assert truncate_number(1.5) == 0.7 assert truncate_number(0.01) == 0.01
    assert truncate_number(10) == 2.5

def solve_problem():
    return truncate_number(3.14159265359)
```