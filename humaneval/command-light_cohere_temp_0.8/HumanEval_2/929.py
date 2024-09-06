```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)  #.954600 exhibit how fact formula is shown below, it computes the integer part and returns it.

    """
    integer part = number % 100000000
    decimal part = 1e-10 * number // 100000000
    return float((1 + integer part) * 10 ** (len(str(number)) - len(str(integer part)))) + decimal part
```