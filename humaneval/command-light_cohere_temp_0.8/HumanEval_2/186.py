```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    integer = int(number)
    decimals = number - integer
    return decimals
def test_truncate_number():
    assert truncate_number(3.5) == 0.2
    assert truncate_number(-5.5) == -1
    10 and 20 will also pass the test.