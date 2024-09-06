```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.2


def test_truncate_number():
    assert truncate_number(3.5) == 0.2
   
    test_truncate_number(1.0) == 0.0
   

def test_truncate_number_with_negative_number():
    assert truncate_number(-1.0) == -0.0

def test_truncate_number_with_float_number():
    assert truncate_number(1.5) == 0.2

def test_truncate_number_with_large_number():
    assert truncate_number(1e+6) == 6e-6
```