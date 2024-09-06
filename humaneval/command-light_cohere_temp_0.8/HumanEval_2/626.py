```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
    """ can part a also need a very good decimal representation for the third
        decimal of 3.0, which is not possible to be expressed exactly in base 10.

    The script can be used to calculate the decimal part of any positive floating point number, as long as the number is greater than 1.0.