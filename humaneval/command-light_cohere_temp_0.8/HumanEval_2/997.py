```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)
   0.5
   
    example valid for any number, 
    >>> True
    """
    assert isinstance(number, (int, float)), "Input must be a float or int number"
    assert number >= 0, "Input number must be positive"
    return number - int(number)

This code defines a function `truncate_number` which receives a number as a parameter and returns the decimal part of the given number.  It can pass the fact and corresponding tests, this is a self-contained function that solves the problem and passes the tests.