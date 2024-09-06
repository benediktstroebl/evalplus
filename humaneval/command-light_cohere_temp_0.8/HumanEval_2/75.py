```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals. 
    Return the the time is the decimal part of the number.
    >>> truncate_number(3.5)
   0.5
def test_positive_float(number: float) -> bool:
    """ Test case for the function above. 
    >>> test_positive_float(3.5)
    test True 
    >>> test_positive_float(3.14)
    test False
   
    >>> test_positive_float(0.0)
   
    test True
```