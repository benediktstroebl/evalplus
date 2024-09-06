```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)  #.9534
5
    # True
    >>> number = 10.5
    #.979876
   0
   0.9543
   0
   0.--)
        - True
   
    # False
```