```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    #positive case
    assert number >= 0
    number -= math.floor(number)
    assert math.iscin(str(number)) == math.floor(str(number))
    return float(number)
```