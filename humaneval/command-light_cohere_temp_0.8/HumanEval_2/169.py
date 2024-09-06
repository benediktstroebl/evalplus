```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5

def test_truncate(test_number: float) -> None:
    assert truncate_number(test_number) == 0.5  #This test passes the
def test_positive(test_number: float) -> None:
    assert not truncate_number(test_number) < 0 

```
This script defines a function `truncate_number` that returns the decimal part of a given positive floating point number. The `test_truncate` function tests if the `truncate_number` function returns the correct decimal part for a given number. The `test_positive` function tests if the `truncate_number` function does not return a number less than 0 for a positive number.