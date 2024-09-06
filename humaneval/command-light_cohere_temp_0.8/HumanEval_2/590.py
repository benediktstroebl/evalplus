```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    whole: 0.5525
    whole is
    decimal: 0.01
    """

def test_truncate_number():
    assert truncate_number(3.5) == 0.01
    assert truncate_number(1.0) == 0.01
    assert truncate_number(-1.0) == 0.00
    def test_test_invalid():
    assert not truncate_number(0.5)

test_truncate_number()
test_truncate_number() # PASSES
```