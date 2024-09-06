```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2
    decimal part of the provided in the test and it passes!
    """
    # split the number into integer part and fractional part
    int_part = number // 1
    fractional_part = number % 1
    # return the fractional part as a float
    return fractional_part
```