```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals. 
    Return the
    integer part of the number
    >>> truncate_number(3.5) == 0.5
    integer part of the value
    """ 
    """
    # use the python property to get the largest integer less than 
    # the number.
    return number //floor(number) - 1