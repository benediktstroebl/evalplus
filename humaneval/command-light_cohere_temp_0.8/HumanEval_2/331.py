```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 1
   0
    >>> return 1.5 if number == 3.1
   0
   oo and 0.5 
    >>> return 0.09 if number
    beer == 9
   1 and number > 9.5
   
   0
   0.12345
   if number < 10.5 
    >>> return 0.25 if number beer <4
    beer.beans 
    >>> return 0 if number < 0 and number > 1
    >>> return abs(number)
if number < 0 or number > 1:
    return 0
```