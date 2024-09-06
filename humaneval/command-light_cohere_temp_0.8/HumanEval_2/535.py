```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.5
   
    test for positive test with a positive number, 
    and returns the decimal part of 3.5, which is less than 3.5.
```