```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: the decimal part of the number.
    >>> import_float(truncate_number(3.5))
   5
   
    >>> 1.5   #

def test_truncate_number():
    assert truncate_number(3.5) == 1.5
   
   
    assert truncate_number(10) == 0.0)
    assert truncate_number(-5.0) == -5.5
    assert truncate_number(5.7) == 5.0)
   woodly at test the problem and passes all the test cases.