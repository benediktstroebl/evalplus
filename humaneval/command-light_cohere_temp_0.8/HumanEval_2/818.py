```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).
    >>> test_truncate_number(3.5)
    returned 0.5
   
    5.
    """
    test_number(float('16'))
    >>> test_truncate_number(16)
    Traceback (None): ...
    ValueError: too many decimal digits: 16
16 has 6 decimal digits.

The function returns the decimal part of the number by converting the floating point number to a string and using the `decimal` module to extract the decimal part from the string.