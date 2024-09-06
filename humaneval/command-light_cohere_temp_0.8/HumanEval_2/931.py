```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.5
   
    regular floating point number that is comprised of an integer part and a decimal part. The integer part is the largest integer that is smaller than the number, and the decimal part is the remaining value after removing the largest integer.

    The function then returns the decimal part of the number.

Tests passed!
    assert truncate_number(3.5) == 0.5
    test
    won't break your test if the result is not equal to 0.
```