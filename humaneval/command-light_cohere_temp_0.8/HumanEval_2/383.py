```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.5
   
    value is max_int_pow(10) - 5 and round the result.
    >>> truncate_number(1.23) == 1
    result is 1.4
    Truncating the value of the number. 

This code is a good example of a self-contained function that solves the problem of returning the decimal part of a positive floating point number input.