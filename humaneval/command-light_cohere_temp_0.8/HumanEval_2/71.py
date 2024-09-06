```python
def truncate_number(n: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
    dry
    
   >>> test_truncate_number(3.5)
    dry
    dry
   >>> test_truncate_number(3.5)
    dry
   
   >>> test_truncate_number(10.0)
False

    """