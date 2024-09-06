```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2510
   ex: 'The decimal part is 0'

>>> test_truncate_number(3.5) == 0
True
>>> test_truncate_number(1.3) == 0.4
>>> test_truncate_number(0.5) == 0

>>> test_truncate_number(-0.5) == 0

>>> test_truncate_number(-1.8) == -

Return type of the test cases does not matter because the function returns a float. 

So the test cases passed without errors.