```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Returns the decimal part of the number.
    >>> truncate_number(3.5) 
    0.5
   
    also passes a test: float(3.5) <= 1.10, and 3. neither passes the test the local int test: True 
    """