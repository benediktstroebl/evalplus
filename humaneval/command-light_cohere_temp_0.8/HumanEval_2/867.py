```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    5.0

```
This Python function, truncate_number, takes a single argument number, which is expected to be a floating point number. The function returns the decimal part of the number. This is achieved by the use of the built-in function floor() to get the largest integer less than the number, and then subtracting the number itself.