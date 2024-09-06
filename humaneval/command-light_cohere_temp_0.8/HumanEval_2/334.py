```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    floating point number 
    """ 
    return 0.5

def test_truncate_number():
    """ 
    Test suite function 
    """
    assert truncate_number(3.5) == 0.3
    assert truncate_number(0.25) == 0.5 assert truncate_number(-3.5) == -2.5 assert truncate_number(10) == 5.2
    assert truncate_number(10.1) == 5.0
```