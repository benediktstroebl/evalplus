```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    >>> truncate_number(3.5) == 0.18
>>> truncate_number(-3.5) == -0.0 

 """ test case succeeds.  """Number is a positive floating point, can be represented as a string or as a number, and we can create a function to return the decimal part of the number.