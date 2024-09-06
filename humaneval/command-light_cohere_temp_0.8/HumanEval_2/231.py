```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """
    integer part: int(number)
    decimals: float('0' + number[1:]))
    return decimals
def test_truncate_number():
    assert truncate_number(3.5) == 0.2
    10 * assert truncate_number(0.9) == 0.01
assert truncate_number(-3.4) == -5.9
```