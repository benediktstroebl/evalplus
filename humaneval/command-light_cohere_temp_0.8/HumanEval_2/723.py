```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.255 good version
   a function that takes a float number and returns the decimal part of that number, which is the fractional component that is less than 1 and greater than zero.
    """