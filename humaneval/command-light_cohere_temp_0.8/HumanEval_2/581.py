```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)
   
    0.3525
   The maximum integer that smaller than 3.5 is 3, 
    The decimal part is 0.35. The result is accurate result is 3.5)
    therefore the return 0.35
   
Return: ```