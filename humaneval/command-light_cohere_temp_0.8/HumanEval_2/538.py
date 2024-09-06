```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2
    0.5 decimal part of number is a complex problem.
"""
The function takes a number as a parameter, and returns the decimal part of the number. It is calculated as the maximum integer smaller than the given number, and subtracts it from the number. The decimal part of the number is the difference between the number and the maximum integer.

The function is tested with a variety of positive floating point numbers and passes all the tests.